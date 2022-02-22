import calendar

#create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2021, 8, 0, 0)
print(st)

#create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2021, 8)
print(st)

#Calculate based on the scenarios below
# a team meeting on the first Friday of every month
# to figure out what days that would be for each month
print("Team meetings will be on: ")
for m in range(1,13): #range(1,13) represent month Jan - Dec
    cal = calendar.monthcalendar(2021, m) #m represent month
    weekone=cal[0]
    weektwo=cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))