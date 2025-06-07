import os
from dotenv import load_dotenv

from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
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

# Память чата — обязательно, иначе будет ошибка
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key="answer"  # 🔥 ОБЯЗАТЕЛЬНО!
)

# Acurai prompt template
acurai_prompt = PromptTemplate.from_template("""
You are an expert assistant for system administrators working with X-Road documentation.
Your task is to analyze technical problems, investigate causes, and give clear instructions.

Always follow this reasoning structure internally, but show only the ANSWER to the user.

QUESTION: {question}
TASK: Determine what the user is trying to achieve.
SYMPTOM: Identify any problem or unclear behavior.
CONTEXT: Use relevant documentation and prior context to understand what may be wrong.
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
""")

# Загрузка FAISS индекса
vectorstore = FAISS.load_local(
    folder_path="faiss_index",
    embeddings=OpenAIEmbeddings(api_key=OPENAI_API_KEY),
    allow_dangerous_deserialization=True
)

# Цепочка с памятью и указанием output_key
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    memory=memory,
    return_source_documents=True,
    combine_docs_chain_kwargs={"prompt": acurai_prompt},
    output_key="answer",
    verbose=True
)

# Функция запроса
def enhanced_query(query: str) -> dict:
    result = qa_chain.invoke({
        "question": query,
        "chat_history": memory.chat_memory.messages  # 🧠 обязательно!
    })
    return {
        "answer": result["answer"],
        "source_documents": [
            doc.metadata.get("source", "") for doc in result["source_documents"]
        ],
        "chat_history": memory.chat_memory.messages
    }

# Для консоли
if __name__ == "__main__":
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ("exit", "quit", "выход"):
            break
        response = enhanced_query(user_input)
        print("GPT:", response["answer"])