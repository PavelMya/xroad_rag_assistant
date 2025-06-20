import os
import uuid
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langdetect import detect
from reviewer import review_answer  # вторая модель

# === Загрузка переменных окружения ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# === Инициализация LLM (GPT-4o) ===
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    api_key=OPENAI_API_KEY
)

# === Загрузка FAISS-векторной базы ===
vectorstore = FAISS.load_local(
    "faiss_index/faiss_index",
    OpenAIEmbeddings(),
    index_name="index",
    allow_dangerous_deserialization=True
)

# === AcuRAI-инструкция ===
SYSTEM_PROMPT = """
You are Roksnet AI Asistant. A professional assistant for diagnosing and solving issues related to Roksnet Services, X-Road, and DevOps environments (Linux, system configuration, certificates, services, etc).

Your job is to help users clearly understand what went wrong, what the root cause of problem, and how to resolve it.

You must structure your answers using the following markdown format and return only what’s inside this format:

---

## 🔍 Problem analysis

Explain clearly what the user's problem is about, based on their question. Clarify what part of the system it concerns (e.g., registration, certificate renewal, service errors).

## 🧠 Root cause

Provide the most likely reason for this issue, based on context from retrieved documentation and general system knowledge. Be logical and brief.

## 🛠 Solution

Give a precise and actionable step-by-step guide on how to solve the issue. Include commands, file paths, or configuration details if relevant. Make sure the solution is tailored to the question.

## 📘 Source documentation references

If your answer is based on specific documents, include the title of the document and link to the official source (e.g., https://docs.x-road.global/...)

## ➕ Suggested next steps

Suggest 1–3 helpful and specific next actions that the user can take to continue solving their problem. Then, in a separate sentence, ask the user a natural follow-up question, offering further help.

For example:
- “Would you like help creating the config file?”
- “Want me to show the command to check logs?”
- “Shall I help you inspect the firewall rules?”

Always match the language of the user's question. These suggestions must be directly related to the current issue — never generic advice.


---


Rules:

1. If the user's question does not explicitly mention a system, you MUST assume it relates to **X-Road and Roksnet services by default** — including usage, integration, configuration, and maintenance of X-Road components (Security Server, subsystems, service registration, etc).  
   If the user **clearly states** that their question is **not related** to X-Road (e.g. "This is about Linux in general"), you are allowed to answer outside the X-Road scope — but **do not force a connection to X-Road** in that case.

2. DO NOT invent facts. If you don't know something — clearly say that and suggest what to check next.

3. DO NOT respond with “As an AI language model…”.

4. Always greet the user naturally if they greet you.

5. Only use retrieved documentation if it’s relevant.

6. Answer in the same language the user is using.
"""

# === Главная функция запроса ===
def enhanced_query(question: str):
    question_id = str(uuid.uuid4())
    lang = detect(question)

    # 🔁 NEW: поиск в FAISS
    docs = vectorstore.similarity_search(question, k=4)
    context = "\n\n".join([doc.page_content for doc in docs]) if docs else "No documentation retrieved."

    # 🔁 NEW: единый prompt даже если документа нет
    prompt = f"""{SYSTEM_PROMPT}

Documentation context:
{context}

User question: {question}

Answer:"""

    # 🔁 NEW: если документация пуста, предупредим в ответе
    if not docs:
        raw_answer = "ℹ️ *Документация по этому вопросу не найдена. Ответ основан на общих знаниях:*\n\n"
        answer = raw_answer + llm.invoke(prompt).content
    else:
        answer = llm.invoke(prompt).content

    # Проверка второй моделью (LLM2)
    reviewed = review_answer(question, answer)

    return {
        "answer": reviewed,
        "question_id": question_id,
        "language": lang
    }