def get_earliest(date1, date2):
   
    month1, day1, year1 = map(int, date1.split("/"))        # Split the dates into month, day, and year
    month2, day2, year2 = map(int, date2.split("/"))        # Split the dates into month, day, and year
    
    if year1 < year2:          # Compare the years first if year1 is less than year2 it will return the date1
        return date1
    elif year1 > year2:        # Compare the years first if year1 is greaterthan year2 it will return the date2
        return date2
    else:                      # If the years are equal, compare the months
        if month1 < month2:    # if month1 is lessthan month2 it will return date1
            return date1
        elif month2 < month1:  # if month2 is lessthan month1 it will return date2
            return date2
        else:                  # If the months are equal, compare the days            
            if day1 < day2:    # If day1 is lessthan dat2 it will return date1
                return date1
            else:              # If day1 is greater or equal dat2 it will return date2
                return date2
            

date1, date2 = input("Please enter two dates MM/DD/YYY separated by a space: ").split()
print(get_earliest(date1,date2))

# Input: Please enter two numbers separated by a space: 01/27/1832 01/27/1756
# Output: 01/27/1756