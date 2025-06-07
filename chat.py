import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, initialize_agent

# 🔧 Встроенные функции
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
            return f.read()[-2000:]  # показать только последние 2000 символов
    except Exception as e:
        return f"Error reading log: {str(e)}"

# 📦 Загрузка ключа
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 🔍 Векторная база
embeddings = OpenAIEmbeddings(api_key=api_key)
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# 🤖 Модель
llm = ChatOpenAI(temperature=0, api_key=api_key, model="gpt-4o")

# 🛠️ Инструменты для агента
tools = [
    Tool.from_function(ping_host, name="ping_host", description="Ping a host. Input should be a hostname or IP."),
    Tool.from_function(read_log, name="read_log", description="Read contents of a log file.")
]

# 🧠 Память
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    input_key="question",
    output_key="answer"
)

# 🧾 Инструкции (AcuRAI + Function Calling + Clarifications)
prompt = ChatPromptTemplate.from_messages([
    ("system",
    "You are a professional consultant for X-Road, Linux server infrastructure, and API operations.\n"
    "Your goal is to identify the user's intent and provide precise, technical answers based on documentation.\n\n"
    "You must extract and reason about these fields from the question:\n"
    "- task\n- system\n- symptom\n- context\n\n"
    "Then reply with a JSON object with keys: task, system, symptom, context, answer, confidence (High/Medium/Low).\n"
    "Use examples, logs, commands, or config snippets when possible.\n"
    "If question is unclear — ask for clarification.\n"
    "If issue is outside X-Road (e.g. Linux/system errors) — state it and offer limited help.\n"
    "Never invent answers. Always reply in the same language as the user."),
    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

# 🔗 Основная цепочка
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 6}),
    memory=memory,
    return_source_documents=True,
    output_key="answer",
    combine_docs_chain_kwargs={"prompt": prompt}
)

# 🤖 Агент для tool-based fallback
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="openai-functions",
    verbose=True
)

# 🔁 Обёртка с уточнением и действиями
def enhanced_query(question: str) -> dict:
    result = qa_chain.invoke({"question": question})

    # Уточняющий prompt
    if "please clarify" in result.get("answer", "").lower():
        result["clarify"] = True

    # Функциональные команды
    if any(kw in question.lower() for kw in ["ping", "log", "restart", "uptime", "syslog"]):
        try:
            tool_output = agent.run(question)
            result["tool_output"] = tool_output
        except Exception as e:
            result["tool_output"] = f"⚠️ Tool error: {str(e)}"

    return result