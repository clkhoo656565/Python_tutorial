from calendar import weekday
from datetime import date
from datetime import time
from datetime import datetime

days = ["mon","tue","wed","thu","fri","sat","sun"]
today = date.today()
month = today.strftime('%B')
now = datetime.now()


print(f'Today is week #: {today.weekday()} in month {month}') #Today is week #: 4 in month August
print(f'Which is a: {days[today.weekday()]}') #Which is a: fri
print(now.strftime("The current year is: %Y")) #The current year is: 2021
print(now.strftime("%a, %d %B, %y")) #Fri, 27 August, 21
print(now.strftime("Locale date and time: %c")) #Locale date and time: Fri Aug 27 18:16:32 2021
print(now.strftime("Locale date: %x")) #Locale date: 08/27/21
print(now.strftime("Locale time: %X")) #Locale time: 18:16:32
print(now.strftime("Current time: %I:%M:%S %p")) #Current time: 06:18:09 PM
print(now.strftime("24-hour time: %H:%M")) #24-hour time: 18:18

print(today.strftime("%d-%b-%Y %H:%m:%S"))

print("Tomorrow will be " +days[(today.weekday()+1)])