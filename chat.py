import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_history_aware_retriever, create_retrieval_chain

# Загрузка переменных окружения
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2,
    api_key=OPENAI_API_KEY
)

# Память чата
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Шаблон Prompt
acurai_prompt = PromptTemplate(
    input_variables=["question", "context"],
    template="""
You are an expert assistant for system administrators working with X-Road documentation.
Your task is to analyze technical problems, investigate causes, and give clear instructions.

Always follow this reasoning structure internally, but show only the ANSWER to the user.

QUESTION: {question}
TASK: Determine what the user is trying to achieve.
SYMPTOM: Identify any problem or unclear behavior.
CONTEXT: {context}
ANSWER:
Respond with a clear, structured and helpful answer that includes:

- What the user is trying to do.
- What could be the causes of the problem.
- Steps to investigate the issue (e.g. log file paths, commands).
- Specific instructions to fix or confirm the behavior.
- Example configuration snippets (if needed).
- Mention exact filenames, directories or UI locations (if applicable).

Do not answer too briefly. Avoid generalities. Prioritize technical clarity and completeness.

Only show the ANSWER section in your response.
"""
)

# FAISS retriever
vectorstore = FAISS.load_local(
    folder_path="faiss_index",
    embeddings=OpenAIEmbeddings(api_key=OPENAI_API_KEY),
    allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever()

# Исторически-осведомлённый retriever
retriever_with_memory = create_history_aware_retriever(
    llm=llm,
    retriever=retriever,
    prompt=acurai_prompt
)

# Chain для генерации ответа
document_chain = create_stuff_documents_chain(
    llm=llm,
    prompt=acurai_prompt
)
qa_chain = create_retrieval_chain(
    retriever=retriever_with_memory,
    combine_docs_chain=llm_chain  # это из load_qa_chain(...)
)

# Функция запроса
def enhanced_query(query: str) -> dict:
    result = qa_chain.invoke({
        "question": query,
        "chat_history": memory.chat_memory.messages
    })
    return {
        "answer": result["answer"],
        "source_documents": [
            doc.metadata.get("source", "") for doc in result.get("source_documents", [])
        ],
        "chat_history": memory.chat_memory.messages
    }

# CLI
if __name__ == "__main__":
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ("exit", "quit", "выход"):
            break
        response = enhanced_query(user_input)
        print("GPT:", response["answer"])