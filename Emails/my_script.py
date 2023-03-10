import argparse
import imaplib
import email
import datetime
import sqlite3
import unittest

def get_emails(email_address, password, name_or_duration):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    email_address = 'vinz223665@gmail.com'
    password = 'ugyltbuxtnpmzijl'
    mail.login(email_address, password)
    mail.select('inbox')
    
    search_query = None
    if name_or_duration.isdigit():
        # get emails from the last N days
        date = (datetime.date.today() - datetime.timedelta(days=int(name_or_duration))).strftime("%d-%b-%Y")
        search_query = f'(SINCE "{date}")'
    else:
        # get emails with the specified name in the subject line
        search_query = f'(SUBJECT "{name_or_duration}")'
    
    result, data = mail.search(None, search_query)
    ids = data[0]
    emails = []
    for id in ids.split():
        result, data = mail.fetch(id, "(RFC822)")
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        subject = email_message['subject']
        body = email_message.get_payload(decode=True).decode()
        emails.append((subject, body))
    # return emails
    print("emails")

# def store_emails(emails, database_name):
#     conn = sqlite3.connect(database_name)
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS emails
#                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   subject TEXT NOT NULL,
#                   body TEXT NOT NULL)''')
#     for email in emails:
#         c.execute("INSERT INTO emails (subject, body) VALUES (?, ?)", email)
#     conn.commit()
#     conn.close()

# class TestEmailFetch(unittest.TestCase):
#     def test_email(self):
#         email_address = 'vinz223665@gmail.com'
#         password = 'ugyltbuxtnpmzijl'
#         name_or_duration = "example" # replace with a valid email subject or duration
#         emails = get_emails(email_address, password, name_or_duration)
#         self.assertTrue(len(emails) > 0)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('name_or_duration', help='Name or duration (in days) to search for in email subject line')
#     parser.add_argument('--email', required=True, help='Email address')
#     parser.add_argument('--password', required=True, help='Email password')
#     parser.add_argument('--database', default='emails.db', help='Database name')
#     args = parser.parse_args()

#     emails = get_emails(args.email, args.password, args.name_or_duration)
#     store_emails(emails, args.database)
    
#     unittest.main(argv=[''], exit=False)