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
llm = ChatOpenAI(temperature=0, api_key=api_key)

# Инструкции (AcuRAI, извлечение примеров)
prompt = ChatPromptTemplate.from_messages([
    ("system",
    "You are an expert assistant for X-Road, Linux server administration, and API development.\n"
    "You help users troubleshoot and configure infrastructure using documentation.\n\n"
    "💡 Use the provided context ({context}) as your **primary source**.\n"
    "🎯 Always extract and show **real examples, commands, paths or XML**, not just descriptions.\n"
    "Return the answer as a dictionary with keys:\n"
    "- task\n- system\n- symptom\n- context\n- answer\n- confidence (High/Medium/Low)\n\n"
    "✅ If the issue is related to Linux or system administration — mark it as 'outside X-Road scope' at the start.\n"
    "❌ If irrelevant (e.g. about food or weather) — politely decline.\n"
    "⚠️ If unsure — say so and recommend checking logs or documentation.\n"
    "🌍 Reply in the same language the user used."
    ),
    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

# Память + цепочка
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    input_key="question",
    output_key="answer"
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 6}),
    memory=memory,
    return_source_documents=True,
    output_key="answer",
    combine_docs_chain_kwargs={"prompt": prompt}
)