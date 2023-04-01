# import smtplib
# from email import encoders
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart


# server = smtplib.SMTP('smtp.gmail.com', 25)

# server.ehlo()

# admin_email = 'vinz223665@gmail.com'                                # Define the email addresses of the admin 
# # password = 'ugyltbuxtnpmzijl'                                     # Define the password of the admin 

# with open('password', 'r') as file:
#     password = file.read()

# server.login(admin_email, password)                                 # Login using login credentials 

# customer_emails = ['vinayakMhavannavar@gmail.com.com', 'vahavannavar@gmail.com'] # Define the email addresses of  customers
# cc_emails = ['Promod4562@gmail.com', 'vinayakMhavannavar@gmail.com.com']         # Define the email addresses to be cc'd
# subject = 'Goods Arrival Notification'      # Define the message to be sent
# message = 'Dear Customer,\n\nWe are pleased to inform you that new goods have arrived. Please visit our store to check them out.\n\nBest regards,\n\nYour Company Name'


# msg = MIMEMultipart()                       # Create the email message
# msg['From'] = admin_email
# msg['To'] = ', '.join(customer_emails)
# msg['Cc'] = ', '.join(cc_emails)
# msg['Subject'] = subject
# msg.attach(MIMEText(message, 'plain'))

# server.starttls()
# server.ehlo()
# server.login('admin@example.com', 'your_email_password')
# server.sendmail(admin_email, customer_emails + cc_emails, msg.as_string())



# # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:           # Send the email message
# #     smtp.ehlo()
#     # smtp.starttls()
#     # smtp.ehlo()
#     # smtp.login('admin@example.com', 'your_email_password')
#     # smtp.sendmail(admin_email, customer_emails + cc_emails, msg.as_string())

# print('Email sent successfully')


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


email_from = 'vinz223665@gmail.com'
email_password = 'ugyltbuxtnpmzijl'
email_subject = 'Daily Goods Arrival Notification'
email_body = 'Hello,\n\nThis is to inform you that new goods have arrived in our store today.\n\nThank you for your continued patronage.\n\nBest regards,\nVinayak'

recipients = ['vishalhirandagi33@gmail.com']
# cc_recipients = ['rsrinivas@msystechnologies.com','meghumeghu3@gmail.com']
cc_recipients = ['vinayakhavannavar@msystechnologies.com','promod456@gmail.com']


msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = ', '.join(recipients)
msg['Cc'] = ', '.join(cc_recipients)
msg['Subject'] = email_subject
msg.attach(MIMEText(email_body, 'plain'))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_from, email_password)

server.sendmail(email_from, recipients + cc_recipients, msg.as_string())
print('Email notification sent successfully!')

server.quit()