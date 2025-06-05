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
    "You are an expert assistant for the X-Road system, as well as a skilled Linux system administrator and backend API developer. "
    "Your priorities are:\n"
    "1. Always check the documentation context ({context}) first.\n"
    "2. If no relevant documentation is found, rely on your professional experience **in server administration (Linux)** and **API integration**.\n"
    "3. If the issue is not related to X-Road, **clearly state**: 'This issue does not appear to be caused by X-Road', and suggest likely causes, such as system misconfigurations, firewall issues, missing packages, or API errors — but only if you're confident.\n"
    "4. If you're not confident, say so. Do not invent features or causes.\n"
    "Your responses should be technical, concise, and actionable.\n"
    "Use commands, paths, examples or diagnostics if helpful.\n"
    "Do not discuss topics unrelated to technical systems (e.g., weather, food)."
    ),

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