import os
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

CREDENTIALS_FILE = "credentials.json"  # Use direct file reference

def get_gmail_service():
    """Returns an authenticated Gmail API service instance."""
    creds = Credentials.from_authorized_user_file("token.json", ['https://www.googleapis.com/auth/gmail.readonly'])
    return build('gmail', 'v1', credentials=creds)

def fetch_unread_emails(_=None):
    """Fetches unread emails from Gmail and returns structured data."""
    try:
        service = get_gmail_service()
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
        messages = results.get('messages', [])

        email_data = []
        if messages:
            for msg in messages:
                msg_id = msg['id']
                email_detail = service.users().messages().get(userId='me', id=msg_id).execute()

                headers = email_detail['payload']['headers']
                subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
                sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
                snippet = email_detail.get('snippet', '')

                email_data.append({
                    "Sender": sender,
                    "Subject": subject,
                    "Snippet": snippet,
                    "Direct Link": f"https://mail.google.com/mail/u/0/#inbox/{msg_id}"
                })

        print("Emails Fetched:", email_data)  
        return email_data

    except Exception as e:
        print(f"Error fetching emails: {e}")
        return []


if __name__ == "__main__":
    emails = fetch_unread_emails()
    if emails:
        for email in emails:
            print(f" **{email['Subject']}** - {email['Sender']}")
            print(f"Open in Gmail: {email['Direct Link']}")
            print("-" * 50)
    else:
        print("No unread emails found.")
