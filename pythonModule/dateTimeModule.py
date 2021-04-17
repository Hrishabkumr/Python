import datetime
from datetime import date
from datetime import datetime

mytime = datetime.time(13,30,1,20)
print(type(mytime))

print(mytime.hour)
print(mytime.minute)
print(mytime.microsecond)
print(mytime)

today = datetime.date.today()
print(f'Today :{today}')
print(f'Today date : {today.day}')
print(f'Ctime : {today.ctime()}')

date1 = date(2021,5,6)
date2 = date(2020,5,6)
result = date1-date2
print(f'Day difference {result}')

datetime1 = datetime(2021,12,5,12)
datetime2 = datetime(2020,12,5,10)
result1 = datetime1-datetime2
print(f'Datetime Result : {result1}')

