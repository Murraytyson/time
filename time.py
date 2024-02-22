import time
t = time.localtime(time.time())
localtime = time.asctime(t)
print(f"Current Time: {localtime}")



import calendar

y = 2024 #year
m = 2    #month

#display the calendar
print(calendar.month(y, m))