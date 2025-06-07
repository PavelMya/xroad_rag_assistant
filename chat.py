import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

# 💬 Чат-модель OpenAI
llm = ChatOpenAI(model='gpt-4o', temperature=0)

# 📚 Подгрузка векторной базы
vectorstore = FAISS.load_local("faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever()

# ✅ Улучшенный AcuRAI prompt
acurai_prompt = PromptTemplate.from_template("""
You are a senior assistant for system administrators using X-Road.

Your job is to deeply analyze the user's technical problem and give a complete, precise and practical answer.

Always reason through the following steps (internally), but show only the final ANSWER:

---
QUESTION: {question}
TASK: What does the user want to achieve?
SYMPTOM: What is going wrong?
CONTEXT: Use documentation, known issues, and common misconfigurations.
---

ANSWER: 
Respond as if you were helping a DevOps engineer in production.

Always include:
- ✅ What the user is trying to do.
- 🔍 Possible root causes (numbered list).
- 🔧 Steps to investigate (with file paths, commands, log names).
- 📄 Example config snippets (if applicable).
- 📂 Exact file locations and required permissions.
- 📘 Mention source documentation files.

Style:
- Use markdown formatting (headers, code blocks, bullet points).
- Prefer short, structured blocks over long paragraphs.
- Avoid vague phrases — be concrete.

Only show the ANSWER section in your response.
""")

# 🧠 Память для чата
memory = ConversationBufferMemory(return_messages=True, memory_key="chat_history")

# 🔗 Создание цепочки QA
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    combine_docs_chain_kwargs={
        "prompt": acurai_prompt
    },
    return_source_documents=True,
    verbose=True,
    output_key="answer"
)

def enhanced_query(query: str) -> dict:
    result = qa_chain.invoke({
        "question": query,
        "chat_history": memory.chat_memory.messages
    })
    return result