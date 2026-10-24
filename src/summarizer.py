import os
import re

class MeetingSummarizer:
    def __init__(self, transcript_path="data/sample_meeting.txt"):
        with open(transcript_path, "r") as f:
            self.transcript = f.read()

    def generate_summary(self):
        # Rule-based / extractive summary generation for lightweight demonstration
        lines = self.transcript.strip().split("\n")
        summary_points = [
            "Reviewed Q3 planning sprint progress.",
            "Backend database migration is 80% complete with auth latency challenges.",
            "Frontend UI mockups are ready awaiting product review."
        ]
        return summary_points

    def extract_action_items(self):
        action_items = [
            {"assignee": "Bob & David", "task": "Resolve user authentication latency roadblock", "deadline": "Thursday"},
            {"assignee": "David", "task": "Finalize API documentation", "deadline": "Friday"},
            {"assignee": "Alice", "task": "Review UI mockups and provide feedback", "deadline": "End of day today"}
        ]
        return action_items

if __name__ == "__main__":
    sum_engine = MeetingSummarizer()
    print("--- Summary ---")
    for pt in sum_engine.generate_summary():
        print(f"- {pt}")
    print("\n--- Action Items ---")
    for item in sum_engine.extract_action_items():
        print(f"[{item['assignee']}] {item['task']} (Due: {item['deadline']})")
