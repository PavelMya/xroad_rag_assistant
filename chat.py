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

# ✅ Важно: prompt должен принимать "context" и "question"
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert assistant for the X-Road system, Linux server administration, and API integration. "
     "Your primary responsibility is to assist users with issues and tasks related to X-Road infrastructure, configuration, security, and deployment. "
     "Use the provided documentation context ({context}) as your first and most authoritative source.\n\n"
     "✅ If a question is related to X-Road but not covered in the context, use your domain expertise to answer accurately.\n"
     "✅ If a question is clearly about Linux/server/system topics (e.g., systemctl, ports, memory, network), say this is **outside the scope of X-Road**, but you may cautiously provide help.\n"
     "❌ If the question is off-topic (e.g. food, jokes), **refuse to answer**.\n"
     "⚠️ If you're not sure about something, clearly say that the answer is uncertain and suggest checking logs, documentation, or contacting the system administrator.\n"
     "🎯 Be concise, professional, and helpful. If possible, include real commands, file paths, or configuration examples.\n"
     "Never hallucinate services or APIs that don’t exist in X-Road.\n"),

    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

# Создаём цепочку RAG
# qa_chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     retriever=db.as_retriever(search_kwargs={"k": 4}),
#     return_source_documents=True,
#     chain_type="stuff",
#     chain_type_kwargs={"prompt": prompt}
# )
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    input_key="question",
    output_key="answer"  # <-- обязательно, иначе ошибка
)

# Цепочка
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 4}),
    memory=memory,
    return_source_documents=True,
    output_key="answer"  # <-- обязательно
)