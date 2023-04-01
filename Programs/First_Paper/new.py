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


# def traffic_signal_decorator(func):
#     def wrapper():
#         print("RED : STOP")
#         func()
#         print("YELLOW : SLOW DOWN")
#         func()
#         print("GREEN : GO")
#     return wrapper

# @traffic_signal_decorator
# def traffic_signal():
#     pass

# traffic_signal()


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

# n = int(input())
# for i in range(n+1):
#     for j in range (i):
#         print("*", end = " ")
#         i -=1
#         j -= 1
#     print() 
   

# simulated = ['CCRLU', 'CRLCUC', 'CCCC']
# avl = 0
# nc = 0
# for i in simulated:
#     for j in i:
#         if j == "C" :
#             if avl == 0 :
#                 nc += 1
#             else:
#                 avl += 1
#         elif j == "R":
#             avl -= 1
#         elif j == "L":
#             avl -= 1
#         elif j == "U":
#             avl += 1
#     print(nc)

#     nc = 0
#     avl = 0




# a = "abcdef"
# a = list(a)
# n = len(a)
# k = 2
# for i in range(0,n,2*k):
#     start = i
#     end = min(i+k-1, n-1)
#     while start<end:
#         a[start], a[end] = a[end], a[start]
#         start += 1
#         end -= 1
# print("".join(a))

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# service_obj = Service("D:/web_driver/chromedriver.exe")

# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(service=service_obj, options=options)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# driver.implicitly_wait(15)

# driver.find_element(By.CLASS_NAME,"nav-line-1-container").click()
# driver.find_element(By.ID,"ap_email").send_keys("vishalhirandagi33@gmail.com")
# driver.find_element(By.ID,"continue").click()
# driver.find_element(By.NAME,"password").send_keys("Vishal#1432")
# driver.find_element(By.ID,"signInSubmit").click()
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Dell laptop")
# driver.find_element(By.ID,"nav-search-submit-button").click()
# driver.find_element(By.CLASS_NAME, "s-image").click()
# list_windows = driver.window_handles
# driver.switch_to.window(list_windows[1])
# driver.find_element(By.ID,"add-to-cart-button").click()
# driver.find_element(By.ID, "attach-view-cart-button-form").click()
# driver.find_element(By.ID,"desktop-ptc-button-celWidget").click()
# driver.find_element(By.XPATH,'//*[@id="shipToThisAddressButton"]/span').click()


# # 30. Write an automation script which should automate marking the attendence in Keka portal. Try to automate the marking for your username. This may require you to do extensive research as Keka login is under company. So please do not restrict your exploration.

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# service_obj = Service("D:/web_driver/chromedriver.exe")

# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(service=service_obj, options=options)
# driver.get("https://msys.keka.com/")

# driver.maximize_window()
# driver.implicitly_wait(35)

# driver.find_element(By.CLASS_NAME,"login-option").click()

# driver.find_element(By.ID,"identifierId").send_keys("vhirandagi@msystechnologies.com")

# driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button/span").click()

# driver.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input").send_keys("Vishal#1432")

# driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div').click()

# driver.find_element(By.XPATH,'//*[@id="accordion"]/li[2]').click()

# driver.find_element(By.XPATH,'/html/body/xhr-app-root/div/employee-me/div/ul/li[2]').click()

# driver.find_element(By.XPATH,'/html/body/xhr-app-root/div/employee-me/div/employee-attendance/div/div/div/employee-attendance-stats/div/div[3]/employee-attendance-request-actions/div/div/div/div/div[2]/div/div[2]/a[1]').click()

# driver.find_element(By.XPATH,'/html/body/modal-container/div[2]/div/employee-attendance-working-remotely-request/div[2]/form/div/div/div[1]/div[1]/div[1]/div/span[2]').click()

# today_date = driver.find_element(By.XPATH,'/html/body/bs-daterangepicker-container/div/div/div/div/bs-days-calendar-view[1]/bs-calendar-layout/div[2]/table/tbody/tr[4]/td[3]/span').click()
# today_date = driver.find_element(By.XPATH,'/html/body/bs-daterangepicker-container/div/div/div/div/bs-days-calendar-view[1]/bs-calendar-layout/div[2]/table/tbody/tr[4]/td[3]/span').click()


n = '912319'
res = '0'
for i in range(len(n)):
    val = n[:i]+n[i+1:]
    # print(val)
    if val > res:
        res = val

print(res)

