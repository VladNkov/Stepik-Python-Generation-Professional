from datetime import date, time, timedelta, datetime


def fill_up_missing_dates(dates):
    days_list = []
    ordinal_days = []
    dates_list = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), dates))
    for i in range(len(dates_list)):
        ordinal_days.append(dates_list[i].toordinal())
    days_list.append(min(ordinal_days))
    new_day = (min(ordinal_days))+1
    days_list.append(new_day)
    while new_day != max(ordinal_days):
        new_day += 1
        days_list.append(new_day)
    answer_list = []
    for d in days_list:
        answer_list.append(date.fromordinal(d))
    return list(map(lambda x: datetime.strftime(x, '%d.%m.%Y'), answer_list))


dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']

print(fill_up_missing_dates(dates))