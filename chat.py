import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory

# Загрузка API-ключа
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Загружаем векторную базу
embeddings = OpenAIEmbeddings(api_key=openai_api_key)
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# LLM с инструкцией
llm = ChatOpenAI(temperature=0, api_key=openai_api_key)

# Обновлённые инструкции
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert assistant for the X-Road system, Linux system administration, and API development. "
     "Your primary responsibility is to assist users with issues and questions related to X-Road infrastructure, configuration, deployment, and troubleshooting. "
     "Use the provided documentation context ({context}) as your most trusted source of truth.\n\n"
     
     "✅ If the question is about X-Road and covered in the documentation, answer based strictly on that.\n"
     "✅ If the question is about X-Road but not covered in the documentation, use your technical knowledge — but stay within the domains of X-Road, Linux servers, APIs, and system deployment.\n"
     "📌 If the question is NOT related to X-Road and appears to be about general system, network, or hardware issues, always begin your reply with:\n"
     "\"📌 This issue appears to be outside the scope of X-Road documentation.\"\n"
     "Then, and only if applicable, you may cautiously suggest what might be the cause. Do not hallucinate.\n"
     "❌ If the question is off-topic (e.g., weather, food, jokes), politely refuse to answer.\n\n"
     
     "⚠️ If you're not sure about the correct answer, say so — and suggest checking logs, documentation, or consulting a system administrator.\n"
     "🎯 Always be concise, technical, and helpful. Where useful, include Linux commands, config file paths, or example output.\n"
     "NEVER invent services, APIs, or behaviors that don’t exist in X-Road.\n"),

    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

# Создаём цепочку RAG
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    input_key="question",
    output_key="answer"  # <-- обязательно, иначе ошибка
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 4}),
    memory=memory,
    return_source_documents=True,
    output_key="answer"  # <-- обязательно
)