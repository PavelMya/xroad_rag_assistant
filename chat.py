import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.prompts import PromptTemplate
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

# Подгружаем индекс
vectorstore = FAISS.load_local(
    folder_path="faiss_index",
    embeddings=OpenAIEmbeddings(api_key=OPENAI_API_KEY),
    allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever()

# Твой кастомный промпт
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

# Создаём retriever с историей
retriever_with_history = create_history_aware_retriever(
    llm=llm,
    retriever=retriever,
    prompt=acurai_prompt
)

# Основная цепочка: сначала достаём документы, затем обрабатываем
qa_chain = create_retrieval_chain(
    retriever=retriever_with_history,
    combine_docs_chain_kwargs={"prompt": acurai_prompt}
)

# Создаём функцию для получения истории
def get_memory(session_id: str) -> BaseChatMessageHistory:
    return ChatMessageHistory()

# Оборачиваем цепочку с памятью
qa_chain_with_memory = RunnableWithMessageHistory(
    qa_chain,
    get_session_history=get_memory,
    input_messages_key="input",
    history_messages_key="chat_history"
)

# Основная функция
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
        user_input = input("Вы: ")
        if user_input.lower() in ("exit", "quit", "выход"):
            break
        response = enhanced_query(user_input)
        print("GPT:", response["answer"])