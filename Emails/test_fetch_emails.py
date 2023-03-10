# import fetch_emails
# import unittest
# import sqlite3

# class TestEmails(unittest.TestCase):
#     def test_emails(self):
#         conn = sqlite3.connect('emails.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT COUNT(*) FROM emails")
#         count = cursor.fetchone()[0]
#         self.assertGreater(count, 0)

# if __name__ == '__main__':
#     unittest.main()


