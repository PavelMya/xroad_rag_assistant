import os
import uuid
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import create_history_aware_retriever, create_retrieval_chain

from reviewer import review_answer
from database import init_db, save_interaction  # 👈 База данных

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Init database
init_db()

# Initialize the OpenAI model
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2,
    api_key=OPENAI_API_KEY
)

# Load FAISS vector store
vectorstore = FAISS.load_local(
    folder_path="faiss_index",
    embeddings=OpenAIEmbeddings(api_key=OPENAI_API_KEY),
    allow_dangerous_deserialization=True
)

# Initialize memory for chat history
memory = ConversationBufferMemory(
    return_messages=True,
    memory_key="chat_history"
)

# --- AcuRAI SYSTEM PROMPT ---
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

# --- AcuRAI Persona ---
acurai_persona_instruction = SystemMessage(
    content="""
You are an AI consultant specializing in X-Road and system administration.

You are NOT a general-purpose assistant. Your role is to help engineers and administrators with topics like:
- X-Road installation, configuration, ACME, logs, and errors,
- APIs, DevOps, Linux, and infrastructure issues.

Even for non-technical questions, maintain your "persona":
- Explain that you're an X-Road assistant.
- Do NOT say you can talk about anything.
- Avoid phrases like "I can answer any question", even if asked about weather or cats.

Style:
- Friendly but professional.
- Give clear, focused responses without unnecessary chatter.
- Be respectful and concise.
- Always remember: you're a technical assistant, not a general AI.
"""
)

# --- AcuRAI Prompt ---
acurai_prompt = ChatPromptTemplate.from_messages([
    acurai_system,
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

# --- Retriever ---
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

# --- Friendly chain ---
def friendly_chain(user_input, chat_history):
    response = llm.invoke([
        acurai_persona_instruction,
        *chat_history,
        ("human", user_input)
    ])
    return response.content

# --- Classification ---
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

# --- Enhanced query with DB + reviewer ---
def enhanced_query(query: str, session_id="default", client_id="0") -> dict:
    # 1. Answer from GPT
    if is_technical_llm(query):
        result = acurai_chain.invoke({
            "input": query,
            "chat_history": memory.chat_memory.messages
        })
        raw_answer = result["answer"].content if hasattr(result["answer"], "content") else str(result["answer"])
    else:
        raw_answer = friendly_chain(query, memory.chat_memory.messages)

    # 2. Pass through reviewer
    reviewed_answer = review_answer(raw_answer)

    # 3. Save to memory
    memory.chat_memory.add_user_message(query)
    memory.chat_memory.add_ai_message(reviewed_answer)

    # 4. Save to DB and get question_id
    question_id = save_interaction(
        question=query,
        answer_llm1=raw_answer,
        answer_llm2=reviewed_answer,
        session_id=session_id,
        client_id=client_id
    )

    return {
        "answer": reviewed_answer,
        "question_id": question_id
    }

# --- Console test (debug only) ---
if __name__ == "__main__":
    session_id = str(uuid.uuid4())  # simulate session
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break
        response = enhanced_query(user_input, session_id=session_id)
        print("GPT:", response["answer"])
        print("🧾 Question ID:", response["question_id"])