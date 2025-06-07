from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from chat import enhanced_query, agent

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    return FileResponse("static/index.html")

class Question(BaseModel):
    question: str

@app.post("/chat")
async def chat_endpoint(q: Question):
    result = enhanced_query(q.question)
    answer = result.get("answer", "").strip()
    task = result.get("task", "").strip()

    # fallback, если GPT ничего не понял
    if not answer or answer.lower().startswith("i don't know") or (not task and "error" in answer.lower()):
        try:
            agent_answer = agent.run(q.question)
            return JSONResponse({
                "answer": f"🛠️ {agent_answer}",
                "task": "Function calling",
                "system": "",
                "symptom": "",
                "context": "",
                "confidence": "High",
                "sources": []
            })
        except Exception as e:
            return JSONResponse({
                "answer": f"⚠️ Tool failed: {str(e)}",
                "task": "Function call failed",
                "system": "",
                "symptom": "",
                "context": "",
                "confidence": "Low",
                "sources": []
            })

    return JSONResponse({
        "answer": answer,
        "task": task,
        "system": result.get("system", ""),
        "symptom": result.get("symptom", ""),
        "context": result.get("context", ""),
        "confidence": result.get("confidence", ""),
        "sources": []  # скрыты от пользователя
    })