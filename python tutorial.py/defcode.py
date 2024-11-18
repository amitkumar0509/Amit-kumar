# number of days in month and first place holder is for index purpose
month_days=[0,31,28,30,30,31,30,31,30,31,30,31,30,31]

def is_leap(year):
# ***return true or false statement for leap an non leap year .***
    return year % 4==0 
def days_in_month(year,month):
    if not 1<= month <=12:
        return 'invalid month'
    if month==2 and is_leap(year):
        return 29
    return month_days[month]
print(is_leap(2020))
print(days_in_month(2012,2))
    
        