def to_percent(ratio):
    percent = round(ratio * 100, 1)
    return f" Percentage is: {percent}%" 

percentage = float(input("Enter the Ratio: "))
print(to_percent(percentage))                   #0.75 = 75.0%, 0.12345='12.3%', 1='100.0%' ,0.5='50.0%'
