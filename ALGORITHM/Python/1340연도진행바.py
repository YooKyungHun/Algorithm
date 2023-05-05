from datetime import datetime

dic = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

month, day, year, time = input().split()
month = dic[month]
day = int(day[0:2])
year = int(year)
hour, minute = map(int, time.split(':'))
# print(month, day, year, hour, minute)
# 5 10 1981 0 31

# year, month, day 세 개는 필수
now = (datetime(year=year, month=month, day=day, hour=hour, minute=minute))
first = datetime(year=year, month=1, day=1)
year = datetime(year=year, month=12, day=31) - datetime(year=year-1, month=12, day=31)
# print('now: ', now, 'first: ', first, 'year: ', year)
# now:  1981-05-10 00:31:00
# first:  1981-01-01 00:00:00
# year:  365 days, 0:00:00

print((now-first) * 100 / year)