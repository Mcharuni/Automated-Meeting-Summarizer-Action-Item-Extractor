# Automated Meeting Summarizer & Action-Item Extractor

An NLP-powered pipeline that ingests meeting transcripts or audio logs, generates concise summaries, and automatically extracts structured action items with assignees and deadlines.

## Features
- Extractive & Abstractive Meeting Summarization
- Automated Action Item and Deadline Tracker
- FastAPI REST backend for integration with virtual meeting tools

## Project Structure
```text
meeting_summarizer_app/
├── data/
│   └── sample_meeting.txt
├── src/
│   ├── summarizer.py
│   └── app.py
├── requirements.txt
└── README.md
```

## Quick Start
1. Install requirements: `pip install -r requirements.txt`
2. Run summarizer script: `python src/summarizer.py`
3. Start API server: `uvicorn src.app:app --reload`
