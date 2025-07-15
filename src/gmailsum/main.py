#!/usr/bin/env python
import sys
import warnings
import os
from flask import Flask, render_template
from dotenv import load_dotenv

# Ensure the correct module path is included
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Import email fetching and CrewAI modules
from src.gmailsum.gmail_api import fetch_unread_emails  # emails before CrewAI runs
from src.gmailsum.crew import Gmailsum  

# Load environment variables
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

app = Flask(__name__)

def categorize(emails):
    """Categorize fetched emails based on sender and subject."""
    categories = {
        "High Priority": [],
        "Medium Priority": [],
        "Low Priority": [],
        "Personal": [],
        "Uncategorized": []
    }

    high_priority_keywords = ["urgent", "asap", "immediate action", "critical", "eod", "interview"]
    medium_priority_keywords = ["action required", "manager","bank","card","purchase"]
    low_priority_keywords = ["newsletter", "promo", "sale", "discount","feedback"]
    personal=["friend","personal"]

    for email in emails:
        subject = email.get("Subject", "").lower()
        snippet = email.get("Snippet", "").lower()  
        sender = email.get("Sender", "").lower()

        
        print(f"Checking Email, Subject: '{subject}', Snippet: '{snippet}', Sender: '{sender}'")

        # Check for High Priority (Keywords in subject or snippet OR sender contains HR/CEO)
        if any(word in subject for word in high_priority_keywords) or any(word in snippet for word in high_priority_keywords) or "hr" in sender or "ceo" in sender:
            print("Classified as HIGH PRIORITY")
            categories["High Priority"].append(email)

        elif any(word in subject for word in medium_priority_keywords) or any(word in snippet for word in medium_priority_keywords) or "manager" in sender:
            print("Classified as MEDIUM PRIORITY")
            categories["Medium Priority"].append(email)

        elif any(word in subject for word in low_priority_keywords) or any(word in snippet for word in low_priority_keywords) or "newsletter" in sender or "promotion" in sender:
            print("Classified as LOW PRIORITY")
            categories["Low Priority"].append(email)

        elif "family" in sender or "friend" in sender or any(word in snippet for word in personal) or any(word in subject for word in personal):
            print("Classified as PERSONAL")
            categories["Personal"].append(email)

        else:
            print("Classified as UNCATEGORIZED")
            categories["Uncategorized"].append(email)

    return categories  

def run():
    """
    Fetch unread emails and categorize them before CrewAI starts.
    """
    try:
        print("Fetching unread emails from Gmail...")
        unread_emails = fetch_unread_emails()  # Fetch emails first

        print("Categorizing emails...")
        categorized_emails = categorize(unread_emails)  # Categorize emails locally

        print(" Categorized Emails:", categorized_emails)

        return categorized_emails  # Return categorized emails instead of letting CrewAI handle it

    except Exception as e:
        print(f" Error occurred: {e}")
        return {}

@app.route('/')
def dashboard():
    """
    Fetch unread emails, categorize them, and display them in the Flask web UI.
    """
    emails = run()  # Fetch & categorize emails 
    return render_template("dashboard.html", emails=emails)

if __name__ == "__main__":
    """
    Start Flask Web App
    """
    print(" Running Flask web app at http://localhost:5000")
    app.run(debug=True)
