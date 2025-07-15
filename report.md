Unfortunately, I am unable to directly access or retrieve emails from external systems like Gmail. However, I have provided a structured plan and Python code example to help you retrieve unread emails using the Gmail API. This solution will guide you through setting up a Google Cloud project, authenticating via OAuth, and executing a script to list unread emails, including the sender, subject, snippet, and a link to the email.

To classify your emails into High, Medium, Low, or Personal priority, you can adapt the code to include logic for analyzing the subject lines and sender information based on the criteria you've listed: 

- High Priority: Keywords "urgent", "ASAP", "immediate action", "critical" or emails from CEO, HR.
- Medium Priority: Emails from managers or containing actionable requests.
- Low Priority: Newsletters, promotions, automated messages.
- Personal: Emails from friends, family, or known contacts.

Once you've retrieved the emails using the code, you can apply these rules to categorize them appropriately. If you implement additional logic in Python, you can automate the classification process as per your requirements.