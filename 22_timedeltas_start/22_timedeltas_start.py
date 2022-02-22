from datetime import time, timedelta, date
from datetime import datetime

print(timedelta(days=365, hours= 5, minutes = 1))

now = datetime.now()
print("today is: " + str(now))

print("One year from now it wil be: " +str(now + timedelta(days = 365)))

#create a timedelta that uses more than one argument
print("In 2 days and 3 weeks, it will be " +
    str(now + timedelta(days = 2, weeks= 3)))

#calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
print(f'The default format of the date 1 week ago {t}') #2021-08-20 20:14:04.000920

s = t.strftime("%A %B %d, %Y")
print(f'The after formatting of the date 1 week ago {s}') #Friday August 20, 2021

#Calculate how many days until April Fools' day?
today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
    print(f"April Fool's day already went %d days ago" % ((today-afd).days))
    afd = afd.replace(year = today.year + 1)

#Now calculate the amount of time until next April Fool's DAy
time_to_afd = afd-today
print(f"The coming April Fool's day is just %d days" % ((time_to_afd).days))