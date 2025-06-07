import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, initialize_agent

# 🔧 Встроенные действия
def ping_host(host: str) -> str:
    import subprocess
    try:
        output = subprocess.check_output(["ping", "-c", "1", host], stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e.output.decode()}"

def read_log(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()[-2000:]
    except Exception as e:
        return f"Error reading log: {str(e)}"

# 📦 API ключ
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 🧠 Векторная база
embeddings = OpenAIEmbeddings(api_key=api_key)
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# 🤖 Модель
llm = ChatOpenAI(temperature=0, api_key=api_key, model="gpt-4o")

# 🛠️ Инструменты
tools = [
    Tool.from_function(ping_host, name="ping_host", description="Ping a host. Input: hostname as string."),
    Tool.from_function(read_log, name="read_log", description="Read contents of a log file.")
]

# 💬 Инструкция (в стиле AcuRAI)
prompt = ChatPromptTemplate.from_messages([
    ("system",
    "You are a senior system consultant for X-Road, Linux server infrastructure, and API integrations. "
    "You act as a smart assistant who can analyze user's intent deeply and provide technical, confident guidance based on documentation context and expertise.\n\n"

    "You must always extract and reason about the following from user input:\n"
    "- task: what the user is trying to achieve or debug\n"
    "- system: component involved (e.g. Security Server, Central Server)\n"
    "- symptom: what is going wrong (e.g. service fails, CORS error)\n"
    "- context: constraints, environment, versions, user role, etc.\n\n"

    "Then reply with a dictionary containing:\n"
    "task, system, symptom, context, answer, confidence (High/Medium/Low)\n\n"

    "💡 Use context chunks as your **primary source**. Quote or summarize real examples, commands, config sections, logs, XML if helpful.\n"
    "✅ If question relates to X-Road, use your knowledge + context.\n"
    "📌 If issue is outside X-Road (e.g. Ubuntu networking, systemd logs), clearly state: 'This appears outside X-Road scope' and offer advice.\n"
    "❌ If question is unrelated (e.g. cooking, philosophy), politely decline.\n"
    "⚠️ If uncertain, say so and recommend verifying logs, restarting services, or contacting an administrator.\n\n"

    "You should ask for clarification if the question is ambiguous, e.g. 'Which OS are you running this on?'\n"
    "Always respond in the **same language as the question**. "
    "Keep tone professional and focused, like a technical expert, not a chatbot.\n"
    "Never invent non-existent APIs or features. Be precise and reliable.")
    ,
    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

# 🧠 Память
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    input_key="question",
    output_key="answer"
)

# 🔍 Основная цепочка RAG
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 6}),
    memory=memory,
    return_source_documents=True,
    output_key="answer",
    combine_docs_chain_kwargs={"prompt": prompt}
)

# 🤖 Agent (для будущего — можно вызывать вместо RAG)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="openai-functions",
    verbose=True
)

# ✅ Поддержка уточнений и команд
def enhanced_query(question: str) -> dict:
    """Обёртка над цепочкой RAG + функция уточнений и действий"""
    response = qa_chain.invoke({"question": question})

    # Если GPT сам просит уточнить
    if "please clarify" in response.get("answer", "").lower():
        response["clarify"] = True

    # Если вопрос похож на команду
    command_keywords = ["ping", "log", "read", "restart", "disk", "memory"]
    if any(kw in question.lower() for kw in command_keywords):
        try:
            tool_result = agent.run(question)
            response["tool_output"] = tool_result
        except Exception as e:
            response["tool_output"] = f"❌ Tool error: {e}"

    return response