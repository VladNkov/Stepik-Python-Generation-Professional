from datetime import date, time, timedelta, datetime


def num_of_sundays(year):

    date1 = date(year, 12, 31)
    return date1.strftime('%U')


print(num_of_sundays(2021))
print(num_of_sundays(768))