#This Python Program inputs a Year and Month and Outputs Calendar for the corresponding values

import time, calendar

#Month Name Function
def name(s):
    if s == 1:
        return "January"
    elif s == 2:
        return "February"
    elif s == 3:
        return "March"
    elif s == 4:
        return "April"
    elif s == 5:
        return "May"
    elif s == 6:
        return "June"
    elif s == 7:
        return "July"
    elif s == 8:
        return "August"
    elif s == 9:
        return "September"
    elif s == 10:
        return "October"
    elif s == 11:
        return "November"
    else:
        return "December"
    
#Local Time
tim = time.asctime(time.localtime(time.time()))
print("Local time on Machine on Execution: {}".format(tim))

#Calendar
year = int(input("Enter year of Calendar: "))
month = int(input("Enter Month of Calendar: "))
monthname = name(month)
cal = calendar.month(year, month)
print("\n\nCalendar For the month of {}, {}\n".format(monthname,year))
print(cal)
