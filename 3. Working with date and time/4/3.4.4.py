from datetime import date, time, timedelta, datetime

pattern = '%H:%M:%S'
input_time = datetime.strptime(input(), pattern)
start_time = datetime.strptime('00:00:00', pattern)
print(int((input_time-start_time).total_seconds()))