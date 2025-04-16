from datetime import date, time, timedelta, datetime

pattern = '%d.%m.%Y'
input_date = datetime.strptime(input(), pattern)
print(input_date.strftime(pattern))
for i in range(2, 11):
    data_i = input_date + timedelta(days=i)
    print(data_i.strftime(pattern))
    input_date = data_i
