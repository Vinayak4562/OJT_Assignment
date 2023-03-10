import argparse
import imaplib
import email
import sqlite3
import datetime

# class TestEmails(unittest.TestCase):
#     def test_emails(self):
#         conn = sqlite3.connect('emails.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT COUNT(*) FROM emails")
#         count = cursor.fetchone()[0]
#         self.assertGreater(count, 0)

def main():
    parser = argparse.ArgumentParser(description='Fetch emails based on time duration and store in a database.')
    parser.add_argument('duration', type=int, help='Time duration in days')
    parser.add_argument('name', type=str, help='name')
    args = parser.parse_args()

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('vinz223665@gmail.com', 'ugyltbuxtnpmzijl')
    mail.select('inbox')

    _, data = mail.search(None, f'(SINCE {(datetime.date.today() - datetime.timedelta(days=args.duration)).strftime("%d-%b-%Y")})')

    conn = sqlite3.connect('emails.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS emails(id INTEGER PRIMARY KEY AUTOINCREMENT,sender TEXT,subject TEXT,body TEXT)''')

    for num in data[0].split():
        _, data = mail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        sender = msg['From']
        subject = msg['Subject']
        body = ''

        if msg.is_multipart():
            for part in msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    body = part.get_payload(decode=True).decode('utf-8')
                    break
        else:
            body = msg.get_payload(decode=True).decode('utf-8')

        cursor.execute("INSERT INTO emails (sender, subject, body) VALUES (?, ?, ?)", (sender, subject, body))

    conn.commit()
    conn.close()

   
