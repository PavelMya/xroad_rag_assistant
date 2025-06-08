import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import create_history_aware_retriever, create_retrieval_chain

# Загрузка переменных среды
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Инициализация LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2,
    api_key=OPENAI_API_KEY
)

# Векторное хранилище FAISS
vectorstore = FAISS.load_local(
    folder_path="faiss_index",
    embeddings=OpenAIEmbeddings(api_key=OPENAI_API_KEY),
    allow_dangerous_deserialization=True
)

# Память чата
memory = ConversationBufferMemory(
    return_messages=True,
    memory_key="chat_history"
)

# --- SYSTEM PROMPT для AcuRAI ---
acurai_system = SystemMessage(
    content="""
You are a senior assistant for system administrators using X-Road.

Your job is to deeply analyze the user's technical problem and give a complete, precise and practical answer.

Always reason through the following steps (internally), but show only the final ANSWER.

---
ANSWER:
✅ What the user is trying to do
🔍 Possible root causes (numbered list)
🔧 Steps to investigate:
- With **commands**, **paths**, **logs**
- What to look for (e.g., errors, confirmation lines)
📄 Example config snippets (if applicable)
📂 Exact file locations and required permissions
📘 Source documentation references (with filenames or markdown anchors)
🧪 Can the issue be verified via CLI or UI?
🪵 What logs to check?
⚠️ Are there tricky or common mistakes?

Style:
- Use markdown formatting (headers, code blocks, bullet points)
- Use emoji bullets for clarity
- Avoid vague phrases — be concrete

Only output the ANSWER section. Do not show your reasoning process.
"""
)

# --- PROMPT для AcuRAI режима (без context!) ---
acurai_prompt = ChatPromptTemplate.from_messages([
    acurai_system,
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

# --- PROMPT для дружелюбного режима ---
friendly_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="Ты — дружелюбный помощник. Отвечай просто, естественно и вежливо."),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

# --- Исторически-осознанный retriever ---
retriever = create_history_aware_retriever(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    prompt=acurai_prompt
)

combine_chain = acurai_prompt | llm

acurai_chain = create_retrieval_chain(
    retriever=retriever,
    combine_docs_chain=combine_chain
)

# --- Цепочка для обычного разговора ---
def friendly_chain(user_input, chat_history):
    response = llm.invoke([
        SystemMessage(content="Ты — дружелюбный помощник."),
        *chat_history,
        ("human", user_input)
    ])
    return response.content

# --- Классификация вопроса с помощью LLM ---
def is_technical_llm(question: str) -> bool:
    classification_prompt = [
        SystemMessage(content="You are a classifier. Your job is to decide if a question is technical."),
        ("human", f"""
Question: "{question}"

Is it a technical question about Linux, X-Road, DevOps, APIs, infrastructure or system administration?

Reply only with YES or NO.
""")
    ]
    result = llm.invoke(classification_prompt)
    return "yes" in result.content.strip().lower()

# --- Обработка пользовательского запроса ---
def enhanced_query(query: str) -> dict:
    if is_technical_llm(query):
        result = acurai_chain.invoke({
            "input": query,
            "chat_history": memory.chat_memory.messages
        })
        answer_text = str(result["answer"])  # <-- Исправление
        memory.chat_memory.add_user_message(query)
        memory.chat_memory.add_ai_message(answer_text)
        return {
            "answer": answer_text
        }
    else:
        answer = friendly_chain(query, memory.chat_memory.messages)
        memory.chat_memory.add_user_message(query)
        memory.chat_memory.add_ai_message(answer)
        return {
            "answer": answer
        }
# --- Локальный запуск через консоль ---
if __name__ == "__main__":
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ("exit", "quit", "выход"):
            break
        response = enhanced_query(user_input)
        print("GPT:", response["answer"])