import os
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval_qa import create_retrieval_chain

# 1. Загрузка переменных окружения
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 2. Создание LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2,
    api_key=OPENAI_API_KEY
)

# 3. Загрузка векторной БД
vectorstore = FAISS.load_local(
    folder_path="faiss_index",
    embeddings=OpenAIEmbeddings(api_key=OPENAI_API_KEY),
    allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever()

# 4. Промпт (в формате LangChain 0.1.17+)
acurai_prompt = PromptTemplate(
    input_variables=["context", "input"],
    template="""
You are an expert assistant for system administrators working with X-Road documentation.
Your task is to analyze technical problems, investigate causes, and give clear instructions.

Always follow this reasoning structure internally, but show only the ANSWER to the user.

QUESTION: {input}
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

# 5. Память
memory = ConversationBufferMemory(
    return_messages=True,
    memory_key="chat_history",
)

# 6. Создание цепочек вручную
combine_docs_chain = create_stuff_documents_chain(
    llm=llm,
    prompt=acurai_prompt
)

retriever_with_history = create_history_aware_retriever(
    llm=llm,
    retriever=retriever,
    memory=memory
)

qa_chain = create_retrieval_chain(
    retriever=retriever_with_history,
    combine_docs_chain=combine_docs_chain
)

# 7. Функция запроса
def enhanced_query(query: str) -> dict:
    result = qa_chain.invoke({"input": query})
    return {
        "answer": result["answer"],
        "source_documents": [
            doc.metadata.get("source", "") for doc in result.get("source_documents", [])
        ],
        "chat_history": memory.chat_memory.messages
    }

# 8. Консольный режим
if __name__ == "__main__":
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ("exit", "quit", "выход"):
            break
        response = enhanced_query(user_input)
        print("GPT:", response["answer"])