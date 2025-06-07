import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chains import create_history_aware_retriever, create_retrieval_chain

# Загрузка API-ключа
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Инициализация модели
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2,
    api_key=OPENAI_API_KEY
)

# Подключение FAISS-индекса
vectorstore = FAISS.load_local(
    folder_path="faiss_index",
    embeddings=OpenAIEmbeddings(api_key=OPENAI_API_KEY),
    allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever()

# 🔧 Шаблон только с 'input', потому что 'create_history_aware_retriever' требует это!
contextualize_q_prompt = PromptTemplate(
    input_variables=["input"],
    template="Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.\n\nChat History:\n{chat_history}\nFollow Up Input: {input}\nStandalone question:"
)

# 🧠 Создание retriever с историей
retriever_with_history = create_history_aware_retriever(
    llm=llm,
    retriever=retriever,
    prompt=contextualize_q_prompt
)

# 🔧 Шаблон для комбинирования документов
combine_prompt = PromptTemplate(
    input_variables=["context", "input"],
    template="""
You are an expert assistant for system administrators working with X-Road documentation.
Your task is to analyze technical problems, investigate causes, and give clear instructions.

QUESTION: {input}
CONTEXT: {context}
ANSWER: 
Respond with a clear, structured and helpful answer that includes:

- What the user is trying to do.
- What could be the causes of the problem.
- Steps to investigate the issue (e.g. log file paths, commands).
- Specific instructions to fix or confirm the behavior.
- Example configuration snippets (if needed).
- Mention exact filenames, directories or UI locations (if applicable).

Only show the ANSWER section in your response.
"""
)

# Создание основной цепочки
qa_chain = create_retrieval_chain(
    retriever=retriever_with_history,
    combine_docs_chain_kwargs={"prompt": combine_prompt}
)

# Функция памяти (в RAM, можно заменить на Redis и т.д.)
def get_memory(session_id: str) -> BaseChatMessageHistory:
    return ChatMessageHistory()

# Обёртка с историей
qa_chain_with_memory = RunnableWithMessageHistory(
    qa_chain,
    get_session_history=get_memory,
    input_messages_key="input",
    history_messages_key="chat_history"
)

# Главная функция запроса
def enhanced_query(query: str) -> dict:
    result = qa_chain_with_memory.invoke(
        {"input": query},
        config={"configurable": {"session_id": "user"}}
    )
    return {
        "answer": result["answer"],
        "source_documents": [
            doc.metadata.get("source", "") for doc in result.get("source_documents", [])
        ]
    }

# Консольный режим
if __name__ == "__main__":
    while True:
        query = input("Вы: ")
        if query.lower() in ("exit", "quit", "выход"):
            break
        answer = enhanced_query(query)
        print("GPT:", answer["answer"])