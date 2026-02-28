from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import EvaluationRequest
from decision_engine import evaluate_books

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/evaluate")
def evaluate(data: EvaluationRequest):
    results = evaluate_books(data)
    return {"ranked_books": results}

@app.get("/")
def root():
    return {"message": "Decision Companion API is running"}