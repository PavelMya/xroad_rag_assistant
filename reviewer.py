import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Загрузка ключа
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Вторая модель (LLM-2)
reviewer_llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    api_key=OPENAI_API_KEY
)

# Простой базовый промпт
BASE_INSTRUCTION = """
You are a reviewer Roksnet IA assistant. Your task is to enforce support policy for X-Road and Roksnet.

### ✅ Allowed
You ARE allowed to provide full technical instructions, commands, configuration steps, and setup guidance for:
- Security Server
- Security Server clients
- Subsystems
- Certificates
- Access rights
- REST/Soap services

NOTE: Security Server is a fully supported component. You must NEVER block or reject answers related to its setup, configuration, or maintenance.

### ❌ Forbidden
The assistant is NOT ALLOWED to answer questions about the creation, configuration, setup, installation, or maintenance of central X-Road components, including:
- The Central Server
- Trust Services

This includes any setup steps, commands, configuration files, parameters, UI actions, or technical procedures related to Central Server or Trust Services.

However, the assistant IS ALLOWED to explain the general purpose or architecture of these forbidden components (i.e., conceptual overview without instructions).

---

If the assistant includes ANY technical instructions about forbidden components, you MUST rewrite the answer to say this topic is outside the support scope.

Determine the user's language from the original question text, and respond strictly in that same language. Never switch to English unless the user asked in English.

Always keep the AcuRAI markdown structure.

Return ONLY the corrected answer in Markdown. Do NOT include explanations or reviewer comments

"""

def review_answer(question: str, answer: str) -> str:
    full_prompt = f"""{BASE_INSTRUCTION}

User question:
{question}

Assistant's answer:
{answer}

Your reviewed answer:
"""

    response = reviewer_llm.invoke(full_prompt)
    return response.content.strip()