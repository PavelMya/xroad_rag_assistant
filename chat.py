import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory

# Загрузка ключа
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Векторная база
embeddings = OpenAIEmbeddings(api_key=api_key)
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Модель
llm = ChatOpenAI(temperature=0, model="gpt-4o", api_key=api_key)

# Строгий system prompt
prompt = ChatPromptTemplate.from_messages([
    ("system",
    "You are a senior technical assistant for the X-Road system, Linux server infrastructure, and API integrations.\n\n"
    "You must return your answer as a strict Python dictionary in the following format:\n\n"
    "{\n"
    "  \"task\": \"...\",\n"
    "  \"system\": \"...\",\n"
    "  \"symptom\": \"...\",\n"
    "  \"context\": \"...\",\n"
    "  \"answer\": \"...\",\n"
    "  \"confidence\": \"High\"  // or Medium or Low\n"
    "}\n\n"
    "⚠️ Do NOT use markdown or wrap your answer in triple backticks (```json). Just return the raw dictionary.\n"
    "⚠️ Do NOT return null — if unsure, leave an empty string.\n"
    "✅ Use documentation context provided as `{context}` to enrich your answer with helpful examples or commands.\n"
    "🚫 If the question is off-topic, explain that you can only help with X-Road, server admin, or APIs.\n"
    "💬 Always match the language of the user's question.\n"
    ),
    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

# Память
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    input_key="question",
    output_key="answer"
)

# Основная цепочка
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 6}),
    memory=memory,
    return_source_documents=True,
    output_key="answer",
    combine_docs_chain_kwargs={"prompt": prompt}
)

# Обёртка для app.py
def enhanced_query(user_question: str):
    return qa_chain.invoke({"question": user_question})