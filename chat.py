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

# Обновлённые инструкции с поддержкой AcuRAI-формата
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert assistant for the X-Road system, Linux system administration, and API development.\n"
     "Use the provided documentation context ({context}) as your most trusted source of truth.\n\n"
     "You follow the AcuRAI instruction format internally to understand every user question.\n"
     "Before answering, you ALWAYS interpret the user input by breaking it into these fields:\n"
     "- task: what the user is trying to achieve or fix (e.g. 'troubleshoot service startup')\n"
     "- system: what system or component is involved (e.g. 'X-Road Central Server')\n"
     "- symptom: what is going wrong or being observed (e.g. '502 Bad Gateway')\n"
     "- context: any extra conditions or constraints\n\n"
     "✅ If the issue is X-Road related, use the documentation and your expertise.\n"
     "📌 If it's a general Linux/system issue, begin your reply with:\n"
     "'📌 This issue appears to be outside the scope of X-Road documentation.'\n"
     "Then cautiously suggest possible causes (no hallucination).\n"
     "❌ If the question is unrelated (e.g. food, weather), politely refuse to answer.\n\n"
     "⚠️ Be clear when unsure. Suggest checking logs or consulting system admins.\n"
     "🎯 Include example config, commands, or diagnostics where relevant.\n"
     "Return your response as a dictionary with keys: task, system, symptom, context, answer.\n"
     "Never invent services or commands that don’t exist.\n"
     "You must always reply in the same language as the user's question."),

    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

# Память и цепочка
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
    combine_docs_chain_kwargs={"prompt": prompt}  # применяем AcuRAI prompt
)
