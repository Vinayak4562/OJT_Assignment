""" To determine whether a year is a leap year, follow these steps:

    1) If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
    2) If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
    3) If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
    4) The year is a leap year (it has 366 days).
    5) The year is not a leap year (it has 365 days).     """

def is_leap_year(year):                 # this method Returns True if the given year is a leap year, otherwise False.    
    if year % 4 == 0:
        if year % 100 == 0:             # If the year is evenly divisible by 100 and 400 its Leap Year
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year = int(input("Enter the Year: "))    
leap = is_leap_year(year)
print(leap)                             # Output: 2020=True, 2021=False