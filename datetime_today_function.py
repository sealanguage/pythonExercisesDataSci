#
from datetime import date

t = date.today()

#  t returns
#  datetime.date(2020, 7, 19)


t = t.replace(year=2021)

#  returns datetime.date(2021, 7, 19)

t = date.today()
t.weekday()

# returns 6 (sunday)

t = date.today()
t.replace(month=11)

#  returns datetime.date(2020, 11, 19)


from datetime import date

today = date(2019, 12, 1)
print(today.strftime("%b, %y"))

# returns Dec, 19


from datetime import date

today = date(2019, 12, 1)
print(today.strftime("%W"))

#  why did this return 47  ??


from datetime import date

today = date(2020, 7, 19)
yesterday = date(2020, 7, 18)
print(yesterday - today)

#  returns -1 day, 0:00:00
