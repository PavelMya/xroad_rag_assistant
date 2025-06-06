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

# Векторная база
embeddings = OpenAIEmbeddings(api_key=openai_api_key)
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Модель
llm = ChatOpenAI(temperature=0, api_key=openai_api_key)

# AcuRAI-инструкции
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert assistant for the X-Road system, Linux system administration, and API development.\n"
     "Use the provided documentation context ({context}) as your most trusted source of truth.\n\n"
     "You follow the AcuRAI instruction format internally to understand every user question.\n"
     "Before answering, you ALWAYS interpret the user input by breaking it into these fields:\n"
     "- task: what the user is trying to achieve or fix\n"
     "- system: what system or component is involved\n"
     "- symptom: what is going wrong or being observed\n"
     "- context: any extra conditions or constraints\n\n"
     "✅ If the issue is X-Road related, use the documentation and your expertise.\n"
     "📌 If it's a general Linux/system issue, begin with:\n"
     "'📌 This issue appears to be outside the scope of X-Road documentation.'\n"
     "Then cautiously suggest possible causes.\n"
     "❌ If the question is unrelated (e.g. food, weather), politely refuse.\n\n"
     "⚠️ Be clear when unsure. Suggest checking logs or consulting sysadmins.\n"
     "🎯 Include example config, commands, or diagnostics where relevant.\n"
     "Return your response as a dictionary with keys: task, system, symptom, context, answer, confidence.\n"
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
    combine_docs_chain_kwargs={"prompt": prompt}
)

# Функция для вызова и извлечения нужных полей
def run_query(question: str):
    result = qa_chain.invoke({"question": question})

    # Источники
    sources = []
    for doc in result.get("source_documents", []):
        metadata = doc.metadata
        sources.append({
            "title": metadata.get("title", ""),
            "file": os.path.basename(metadata.get("source", "")) if "source" in metadata else ""
        })

    # Ответ в формате AcuRAI
    if isinstance(result["answer"], dict):
        return {
            "answer": result["answer"].get("answer", ""),
            "task": result["answer"].get("task", ""),
            "system": result["answer"].get("system", ""),
            "symptom": result["answer"].get("symptom", ""),
            "context": result["answer"].get("context", ""),
            "confidence": result["answer"].get("confidence", ""),
            "sources": sources
        }

    return {
        "answer": result["answer"],
        "task": "",
        "system": "",
        "symptom": "",
        "context": "",
        "confidence": "",
        "sources": sources
    }