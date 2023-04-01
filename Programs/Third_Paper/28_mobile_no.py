n = input("Enter your mobile number: ")
str = sorted(n)
if len(str) == 10:
    print("+91-"+"".join(str))
else:
    print("Enter the proper mobile number that consist of 10 digits")