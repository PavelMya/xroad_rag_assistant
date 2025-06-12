from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from starlette.templating import Jinja2Templates
from pydantic import BaseModel
import os

from chat import enhanced_query
from database import mark_incorrect, save_suggested_answer, Interaction, Base, Session

SessionLocal = Session

# === FastAPI App ===
app = FastAPI()

# === CORS ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === DATABASE ===
SessionLocal = Session

# === Static/Template ===
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# === Models ===
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]
    question_id: str

class IncorrectFeedback(BaseModel):
    question_id: str

class SuggestFeedback(BaseModel):
    question_id: str
    suggested_answer: str

# === Pages ===
@app.get("/", response_class=FileResponse)
async def serve_index():
    return "static/index.html"

@app.get("/admin", response_class=HTMLResponse)
def admin_page(request: Request):
    session = SessionLocal()
    interactions = session.execute(
        select(Interaction).order_by(Interaction.timestamp.desc())
    ).scalars().all()
    session.close()
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "interactions": interactions
    })

# === Chat Logic ===
@app.post("/chat", response_model=QueryResponse)
async def chat_endpoint(request: QueryRequest):
    response = enhanced_query(request.question)
    return {
        "answer": response["answer"],
        "sources": [],
        "question_id": response["question_id"]
    }

@app.post("/feedback/incorrect")
async def feedback_incorrect(feedback: IncorrectFeedback):
    mark_incorrect(feedback.question_id)
    return {"status": "ok", "message": "Marked as incorrect"}

@app.post("/feedback/suggest")
async def feedback_suggest(feedback: SuggestFeedback):
    save_suggested_answer(feedback.question_id, feedback.suggested_answer)
    return {"status": "ok", "message": "Suggestion saved"}

# === Admin Forms ===
@app.post("/admin/mark_incorrect", response_class=RedirectResponse)
def mark_incorrect_form(request: Request, question_id: str = Form(...)):
    session = SessionLocal()
    interaction = session.query(Interaction).filter_by(question_id=question_id).first()
    if interaction:
        interaction.is_incorrect = True
        session.commit()
    session.close()
    return RedirectResponse(url="/admin", status_code=303)

@app.post("/admin/suggest_answer", response_class=RedirectResponse)
def suggest_answer_form(
    request: Request,
    question_id: str = Form(...),
    suggested_answer: str = Form(...)
):
    session = SessionLocal()
    interaction = session.query(Interaction).filter_by(question_id=question_id).first()
    if interaction:
        interaction.suggested_answer = suggested_answer
        session.commit()
    session.close()
    return RedirectResponse(url="/admin", status_code=303)

# === Run (optional for local testing) ===
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
