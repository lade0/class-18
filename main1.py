# program to check the currewnt data and time
from datetime import date, time, datetime
today= date.today()
time= datetime.now()
print("todays date is:",today)
print("current date and time is",time)
print("date components",today.year,today.month,today.day)