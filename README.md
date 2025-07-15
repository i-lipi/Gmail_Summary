Gmail Summary & Prioritization AI

This project is an AI-powered system that reads, classifies, and prioritizes unread emails from a Gmail inbox using the Gmail API, CrewAI framework, and intelligent agents. It provides a clean web dashboard where users can view their emails sorted by priority such as High, Medium, Low, Personal, and Uncategorized.


Features:
- OAuth2 Integration with Gmail API (via credentials.json & token.json)
- Secure email fetching using Google’s gmail.readonly scope
- Agent-based architecture powered by CrewAI:
  * email_reader: Fetches unread emails with sender, subject, snippet, and direct Gmail links
  * email_categorizer: Classifies emails using content-based prioritization rules
-Customizable HTML Dashboard: Displays email summaries by category in a styled UI
-Modular design with agent and task configuration defined in YAML
-Security-conscious: .gitignore excludes secret files like token.json, .env, and credentials.json
[You can generate your own through "https://console.cloud.google.com/apis/library/gmail.googleapis.com"]

How It Works
-Authentication: Run gmail_auth.py to authenticate via browser and generate token.json.
-Fetch Emails: The fetch_unread_emails function retrieves unread inbox messages using Gmail API.
-Categorize: Emails are classified into categories using LLM-based logic and keyword rules.
-Display: The categorized emails are rendered in a responsive dashboard (dashboard.html).

Example Output:

High Priority: Emails containing words like “urgent”, “interview”, “critical”
Medium Priority: Managerial instructions or important updates
Low Priority: Newsletters, auto-replies, and subscriptions
Personal: Emails from known friends/family
Uncategorized: Miscellaneous or ambiguous messages

Technologies Used:

Python (Gmail API, OAuth2)
CrewAI (Agent orchestration and task pipelines)
HTML/CSS for dashboard UI
Google API Client
Jinja2 for templating
Markdown reporting (report.md)
