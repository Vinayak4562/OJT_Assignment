import datetime

def meetup_date(year, month):      
    first_day = datetime.date(year, month, 1)       # We first calculate the date for the 1st day of the month
    
    first_day_weekday = first_day.weekday()         # here finding the day of the week for the 1st day of the month
    
    meetup_day = 26 - (first_day_weekday + 1) if first_day_weekday <= 3 else 32 - (first_day_weekday + 1)  # We calculate the number of days to the 4th Thursday of the month
   
    return f'{datetime.date(year, month, meetup_day)}, Meet up Date is {meetup_day}'     # here creating the datetime.date object and returning it 


year = int(input("Enter the Year: "))
month = int(input("Enter the month: "))
print(meetup_date(year,month))

# year:2012
# month:3