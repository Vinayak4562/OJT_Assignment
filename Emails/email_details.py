import argparse
import email
import imaplib
import sqlite3
import unittest

# Set up the argument parser
parser = argparse.ArgumentParser(description='Fetch email details and store in database.')
parser.add_argument('name_or_duration', type=str, help='Name or time duration to search email for')
args = parser.parse_args()

# Connect to the email server
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('vinz223665@gmail.com', 'ugyltbuxtnpmzijl')
mail.select('inbox')

# Search for the email based on the name or time duration supplied through argparse
if args.name_or_duration.isdigit():
    search_criteria = 'SINCE {} day'.format(args.name_or_duration)
else:
    search_criteria = 'FROM "{}"'.format(args.name_or_duration)
result, data = mail.search(None, search_criteria)

# Parse the email and extract the relevant details
if result == 'OK' and len(data[0]) > 0:
    email_ids = data[0].split()
    for email_id in email_ids:
        result, data = mail.fetch(email_id, '(RFC822)')
        if result == 'OK':
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            sender = email.utils.parseaddr(email_message['From'])[1]
            subject = email_message['Subject']
            body = email_message.get_payload(decode=True).decode()
            
            # Store the email details in a database
            conn = sqlite3.connect('email_details.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS email_details (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                     sender TEXT,
                                                                     subject TEXT,
                                                                     body TEXT)''')
            c.execute('INSERT INTO email_details (sender, subject, body) VALUES (?, ?, ?)', (sender, subject, body))
            conn.commit()
            conn.close()

# class TestEmail(unittest.TestCase):
#     def test_email_details(self):
#         # Connect to the database and retrieve the email details
#         conn = sqlite3.connect('email_details.db')
#         c = conn.cursor()
#         c.execute('SELECT sender, subject, body FROM email_details ORDER BY id DESC LIMIT 1')
#         result = c.fetchone()
#         conn.close()

#         # Assert that the email details match the expected values
#         self.assertIsNotNone(result)
#         self.assertEqual(result[0], sender)
#         self.assertEqual(result[1], subject)
#         self.assertEqual(result[2], body)

# if __name__ == '__main__':
#     unittest.main()
