from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
import os

from database_models import Interaction, Base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///interactions.db")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


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


@app.post("/admin/mark_incorrect", response_class=RedirectResponse)
def mark_incorrect(request: Request, question_id: str = Form(...)):
    session = SessionLocal()
    interaction = session.query(Interaction).filter_by(question_id=question_id).first()
    if interaction:
        interaction.is_incorrect = True
        session.commit()
    session.close()
    return RedirectResponse(url="/admin", status_code=303)


@app.post("/admin/suggest_answer", response_class=RedirectResponse)
def suggest_answer(request: Request, question_id: str = Form(...), suggested_answer: str = Form(...)):
    session = SessionLocal()
    interaction = session.query(Interaction).filter_by(question_id=question_id).first()
    if interaction:
        interaction.suggested_answer = suggested_answer
        session.commit()
    session.close()
    return RedirectResponse(url="/admin", status_code=303)