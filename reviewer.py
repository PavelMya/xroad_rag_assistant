from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

reviewer_llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    api_key=OPENAI_API_KEY
)

reviewer_prompt = SystemMessage(
    content="""
You are a reviewer that checks final answers from an AI assistant.

Your job:
1. Analyze the assistant's full response.
2. If it contains speculative or unverifiable content — add a warning at the end.
3. The warning must be written in the **same language** as the original response.
   Use polite, concise wording appropriate to that language and audience.

Examples:
- English: "⚠️ Please note: this part may be uncertain or incomplete."
- (But you must detect the language automatically and adjust!)

⚠️ Do NOT modify or rewrite the main answer.
Only append the warning if necessary.
Do NOT add warnings to greetings, simple or obvious answers.

Your goal is to help ensure trustworthy and transparent communication.
"""
)

def review_answer(answer_text: str) -> str:
    result = reviewer_llm.invoke([
        reviewer_prompt,
        ("human", f"""
Here is the assistant's final response:

\"\"\"{answer_text}\"\"\"

If the response is 100% safe, return it unchanged.
If not, append a language-appropriate warning.
Do not reword the original text.
""")
    ])
    return result.content.strip()
