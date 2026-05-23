from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from retriever import search_assessments

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

@app.get("/")
def home():

    return {
        "message": "SHL Assessment Recommendation API is running successfully"
    }

@app.get("/health")
def health():

    return {
        "status": "ok"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    latest_message = request.messages[-1].content

    if len(latest_message.split()) < 5:

        return {
            "reply": "Can you share more details like role, experience level, technical skills, and whether you need aptitude or personality assessments?",
            "recommendations": [],
            "end_of_conversation": False
        }

    recommendations = search_assessments(
        latest_message
    )

    if not recommendations:

        return {
            "reply": "No matching SHL assessments found for this requirement.",
            "recommendations": [],
            "end_of_conversation": True
        }

    recommendation_names = []

    for rec in recommendations:
        recommendation_names.append(rec["name"])

    reply = (
        "Based on your hiring requirement, "
        "these SHL assessments are recommended: "
        + ", ".join(recommendation_names)
    )

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": True
    }