from datetime import date, timedelta, datetime

pattern = '%d.%m.%Y'
dt = datetime.strptime(input(), pattern)
last_day = dt - timedelta(days=1)
next_day = dt + timedelta(days=1)
print(last_day.strftime(pattern))
print(next_day.strftime(pattern))

