# import math

# print(math.sqrt(-25))  #ValueError


        

# Here's a Python program that prints the pattern every two hours without using the sleep function:

# python
# Copy code


# n = int(input("Enter the number of col: "))
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


def traffic_signal_decorator(func):
    def wrapper():
        print("RED : STOP")
        func()
        print("YELLOW : SLOW DOWN")
        func()
        print("GREEN : GO")
    return wrapper

@traffic_signal_decorator
def traffic_signal():
    pass

traffic_signal()


# RED : STOP
# YELLOW : SLOW DOWN
# RED : STOP
# GREEN : GO
# YELLOW : SLOW DOWN
# GREEN : GO

# names_list = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']

# sorted_names = sorted(names_list)

# print(sorted_names)


# # saturdays in moths
# import calendar

# def Date_saturdays(month, year):
#     saturdays = []
#     _, num_days = calendar.monthrange(year, month)
#     for day in range(1, num_days + 1):
#         if calendar.weekday(year, month, day) == calendar.SATURDAY:
#             saturdays.append(day)
#     return saturdays

# saturdays = Date_saturdays(4, 2023)
# print(saturdays)

# def highest_sum(s):
#     prev_char = ''
#     sum = 0
#     for c in s:
#         if c != prev_char:
#             sum += int(c)
#             prev_char = c
#     return sum

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Customer and CC email addresses
# customers = ['promod456@.gmail.comcom']
# cc_list = ['vishalhirandagi@gmail.com']

# # Sender's email credentials
# sender_email = 'vinayakhavannavar@gmail.com'
# sender_password = '4562#havannavarP'

# # Email message details
# subject = 'Goods Arrival Notification'
# message = 'Dear customer,\n\nWe are pleased to inform you that new goods have arrived. Please visit our store to check them out.\n\nThank you,\nThe Admin Team'

# # Create message object
# msg = MIMEMultipart()
# msg['From'] = sender_email
# msg['To'] = ', '.join(customers)
# msg['Cc'] = ', '.join(cc_list)
# msg['Subject'] = subject
# msg.attach(MIMEText(message, 'plain'))

# # Create SMTP session
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     # Start TLS for security
#     smtp.starttls()
#     # Authenticate with sender's email account
#     smtp.login(sender_email, sender_password)
#     # Send email to customers and cc list
#     smtp.sendmail(sender_email, customers + cc_list, msg.as_string())

# print('Mail sent successfully.')



# # Regular expressions are allow us to search for general pattern in the Text data.
# # re Library allow us to create special pattern strings and then search for    
# # matches with text.
# import re

# data = ["example (.com)", "MSys", "github (.com)", "keka (.com)"]
# reg_exp = r"\s*\([^()]*\)"	# Regular Expression.

# for string in data:
#     result = re.sub(reg_exp, "", string) #re.sub(pattern, repl, string) is used to substitute 
#     print(result)   					#occurrences of a pattern in a string with a replacement string.

	   									 

  
   
