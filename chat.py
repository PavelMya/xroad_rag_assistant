import os
from dotenv import load_dotenv

from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate

# Загрузка переменных окружения
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Настройки модели
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2,
    api_key=OPENAI_API_KEY
)

# Acurai prompt template
acurai_prompt = PromptTemplate.from_template("""
You are an expert technical assistant for X-Road documentation.
Follow the structured reasoning steps below, but output ONLY the final ANSWER to the user.

QUESTION: {question}
TASK: Determine what the user is trying to achieve.
SYMPTOM: Identify any implicit or explicit problem.
CONTEXT: Use the relevant documentation provided below:
{context}
ANSWER: Provide a clear, helpful, and technical answer.
Only return the ANSWER section in your response.
""")

# Загрузка FAISS индекса
vectorstore = FAISS.load_local(
    folder_path="faiss_index",
    embeddings=OpenAIEmbeddings(api_key=OPENAI_API_KEY),
    allow_dangerous_deserialization=True
)

# Создание цепочки без памяти (или можно позже заменить)
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    return_source_documents=True,
    combine_docs_chain_kwargs={"prompt": acurai_prompt},
    output_key="answer",  # Указано явно
    verbose=True
)

# Функция чата
def enhanced_query(query: str) -> dict:
    """Основной метод запроса к модели."""
    result = qa_chain.invoke({
        "question": query,
        "chat_history": memory.chat_memory.messages  # 🔥 ОБЯЗАТЕЛЬНО!
    })
    return {
        "answer": result["answer"],
        "source_documents": [
            doc.metadata.get("source", "") for doc in result["source_documents"]
        ],
        "chat_history": memory.chat_memory.messages
    }

# Тест в консоли
if __name__ == "__main__":
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ("выход", "exit", "quit"):
            break
        response = enhanced_query(user_input)
        print("GPT:", response["answer"])