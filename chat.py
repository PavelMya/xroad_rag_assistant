import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory

# Загрузка API-ключа
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Загружаем векторную базу
embeddings = OpenAIEmbeddings(api_key=openai_api_key)
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Модель
llm = ChatOpenAI(temperature=0, api_key=openai_api_key)

# Инструкция AcuRAI + форматированная структура
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert assistant for the X-Road system, Linux system administration, and API development.\n"
     "Use the documentation context ({context}) as your primary source of truth.\n\n"
     "Always parse the user request into:\n"
     "- task: what the user wants to do\n"
     "- system: what component is involved\n"
     "- symptom: what is happening\n"
     "- context: any extra info\n\n"
     "Return your answer as a dictionary with:\n"
     "task, system, symptom, context, answer, confidence\n\n"
     "✅ If it’s about Linux/system: write 📌 This issue appears to be outside the scope of X-Road.\n"
     "❌ If irrelevant (e.g. food): politely refuse.\n"
     "⚠️ Say you're not sure if needed. Do not invent anything.\n"
     "🧠 Confidence must be High / Medium / Low."),

    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    input_key="question",
    output_key="answer"
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 4}),
    memory=memory,
    return_source_documents=True,
    output_key="answer",
    combine_docs_chain_kwargs={"prompt": prompt}
)