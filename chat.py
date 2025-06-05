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
    "You are an expert assistant for the X-Road system. "
    "Your primary task is to help users understand, troubleshoot, and work with X-Road infrastructure. "
    "Use the provided documentation context ({context}) as your first and most authoritative source. "
    "If no relevant answer is found in the docs, rely on your knowledge — "
    "but strictly within the domains of X-Road, server administration, Linux, configuration, security, or deployment. "
    "If a user's problem suggests a server/system-level issue (e.g., file permissions, missing packages, misconfigured services), you may propose possible causes or suggestions — but clearly indicate that it is outside the documentation scope. "
    "Never answer questions that are completely off-topic (e.g. food, weather, general knowledge). "
    "Never hallucinate; if something is unclear or not documented, say so and recommend next steps (e.g., check logs, restart service, consult administrator). "
    "If a user asks for a command or file path, double-check it against X-Road norms or Unix conventions. "
    "Prefer concise and professional answers with helpful detail. "
    "If appropriate, offer commands, config paths, or example output to help the user debug effectively. "
    "Never invent services, APIs, or behaviors that X-Road does not have. "
    "Be accurate, technical, and focused."),
    
    ("human", "Based on the following documentation context, answer the user question.\n\n"
    "Context:\n{context}\n\n"
    "Question:\n{question}")
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