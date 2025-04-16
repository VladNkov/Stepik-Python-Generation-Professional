from datetime import date, time, timedelta, datetime

pattern = '%H:%M:%S'
input_time = datetime.strptime(input(), pattern)
n = timedelta(seconds=int(input()))
answer = input_time+n
print(answer.strftime(pattern))
