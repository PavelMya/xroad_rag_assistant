import os
from dotenv import load_dotenv

from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# Загрузка переменных окружения
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Настройка модели
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2,
    api_key=OPENAI_API_KEY
)

# Шаблон AcuRAI без переменной {context}

acurai_prompt = PromptTemplate(
    input_variables=["question", "context"],
    template="""
You are a senior assistant for system administrators using X-Road.

Your job is to deeply analyze the user's technical problem and give a complete, precise and practical answer.

Always reason through the following steps (internally), but show only the final ANSWER.

---
QUESTION: {question}
TASK: What does the user want to achieve?
SYMPTOM: What is going wrong?
CONTEXT: {context}
---

ANSWER:
Respond as if you were helping a DevOps engineer in production.

Always include:

✅ What the user is trying to do

🔍 Possible root causes (numbered list)

🔧 Steps to investigate:
- With **commands**, **paths**, **logs**
- What to look for (e.g., errors, confirmation lines)

📄 Example config snippets (if applicable)

📂 Exact file locations and required permissions

📘 Source documentation references (with filenames or markdown anchors)

---

🧪 Can the issue be verified via CLI or UI?
- Say **what to do** in command line
- Say **what to click** in UI

🪵 What logs to check?
- Which **log files**
- What to **search for**

⚠️ Are there tricky or common mistakes?
- What users **frequently miss or misconfigure**

---

Style:
- Use markdown formatting (headers, code blocks, bullet points)
- Use emoji bullets for clarity
- Avoid vague phrases — be concrete

Only show the final ANSWER section in your response.
"""
)

# Память чата
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key="answer"
)

# Векторная база FAISS
vectorstore = FAISS.load_local(
    folder_path="faiss_index",
    embeddings=OpenAIEmbeddings(api_key=OPENAI_API_KEY),
    allow_dangerous_deserialization=True
)

# Цепочка вопрос-ответ
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    memory=memory,
    return_source_documents=True,
    combine_docs_chain_kwargs={"prompt": acurai_prompt},
    output_key="answer",
    verbose=True
)

# Обработка запроса
def enhanced_query(query: str) -> dict:
    result = qa_chain.invoke({
        "question": query,
        "chat_history": memory.chat_memory.messages
    })
    return {
        "answer": result["answer"],
        "source_documents": [
            doc.metadata.get("source", "") for doc in result["source_documents"]
        ],
        "chat_history": memory.chat_memory.messages
    }

# Локальный запуск
if __name__ == "__main__":
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ("exit", "quit", "выход"):
            break
        response = enhanced_query(user_input)
        print("GPT:", response["answer"])