# SHL Assessment Recommendation Chatbot

## Project Overview

This project is an AI-powered SHL Assessment Recommendation System built using FastAPI and Python.

The chatbot helps recruiters or hiring managers find suitable SHL assessments based on hiring requirements such as:
- Job role
- Technical skills
- Communication skills
- Leadership requirements
- Personality assessments

The system supports:
- Conversational recommendation flow
- Clarification handling
- Assessment recommendation
- Comparison queries
- Off-topic query handling

---

# Tech Stack

- Python
- FastAPI
- Pandas
- Uvicorn
- REST API
- CSV-based recommendation engine

---

## Live API

Base URL:
https://shl-assignment-ajuu.onrender.com

Swagger Docs:
https://shl-assignment-ajuu.onrender.com/docs

# Project Structure

```text
shl-assignment/
│
├── main.py
├── retriever.py
├── scraper.py
├── shl_catalog.csv
├── requirements.txt
├── README.md
└── .env
Setup Instructions
1. Clone Project
git clone <repository_url>
cd shl-assignment
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment
Windows
venv\Scripts\Activate.ps1
4. Install Dependencies
pip install -r requirements.txt
Run Application

Start FastAPI server:

uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000

Swagger API documentation:

http://127.0.0.1:8000/docs
API Endpoints
Health Check
GET /health

Response:

{
  "status": "ok"
}
Chat Recommendation Endpoint
POST /chat

Request Body:

{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java developer with communication skills"
    }
  ]
}

Sample Response:

{
  "reply": "Based on your hiring requirement, these SHL assessments are recommended: Java 8 (New)",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "https://www.shl.com",
      "test_type": "Assessment"
    }
  ],
  "end_of_conversation": true
}
Recommendation Logic

The recommendation engine:

Reads SHL assessment catalog from CSV
Matches user query keywords
Scores matching assessments
Returns top recommendations
Features Implemented
Conversational chatbot API
SHL assessment recommendation
Clarification handling
Off-topic query handling
Assessment comparison handling
Swagger documentation
REST API architecture
Future Improvements
Real SHL catalog scraping
Semantic search using embeddings
Vector database integration
LLM-powered recommendations
Frontend UI integration
Deployment on cloud platforms
Author

Meghana DK

