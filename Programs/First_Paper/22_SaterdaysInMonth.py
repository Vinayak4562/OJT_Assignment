# saturdays in moths
import calendar

def get_saturdays_in_month(year,month):    
    saturdays = []
    cal = calendar.monthcalendar(year,month)
    for week in cal:
        if week[calendar.SUNDAY] != 0:
            saturdays.append(week[calendar.SATURDAY])
    return saturdays

print(get_saturdays_in_month(2023,3))