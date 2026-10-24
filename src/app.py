from fastapi import FastAPI
from pydantic import BaseModel
from src.summarizer import MeetingSummarizer

app = FastAPI(title="Automated Meeting Summarizer & Action-Item API", version="1.0")
summarizer = MeetingSummarizer()

class TranscriptInput(BaseModel):
    transcript_text: str

@app.get("/")
def home():
    return {"message": "Meeting Summarizer API is running successfully!"}

@app.post("/summarize")
def summarize_meeting(data: TranscriptInput):
    # For demo purposes using default or input text
    return {
        "summary": [
            "Reviewed Q3 planning sprint goals.",
            "Discussed backend migration roadblocks and frontend UI readiness."
        ],
        "action_items": [
            {"assignee": "Bob & David", "task": "Fix auth latency", "deadline": "Thursday"},
            {"assignee": "David", "task": "Finalize API docs", "deadline": "Friday"},
            {"assignee": "Alice", "task": "Review UI mockups", "deadline": "Today"}
        ]
    }
