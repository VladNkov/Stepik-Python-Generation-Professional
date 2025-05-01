# Функция get_all_mondays()
# Реализуйте функцию get_all_mondays(), которая принимает один аргумент: year — натуральное число
# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year,
# выпадающих на понедельник.
# Примечание 1. Repetition tasks. Например, вызов:
# get_all_mondays(2021)
# должен вернуть список:
#
# [datetime.date(2021, 1. Repetition tasks, 4. Working with files), datetime.date(2021, 1. Repetition tasks, 11), ..., datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_all_mondays(),
# но не код, вызывающий ее.
import calendar
from datetime import date, timedelta


def get_all_mondays(year):

    mondays_list = []
    # n_day = date(year, 1. Repetition tasks, 1. Repetition tasks)
    # for _ in range(7):
    #     if calendar.weekday(n_day.year, n_day.month, n_day.day) == 0:
    #         while n_day.year == year:
    #             mondays_list.append(n_day)
    #             n_day += timedelta(days=7)
    #     n_day += timedelta(days=1. Repetition tasks)

    for month in range(1, 13):
        for week in calendar.monthcalendar(year, month):
            monday = week[0]
            if monday:
                mondays_list.append(date(year, month, monday))

    return mondays_list


result = get_all_mondays(2022)
print(result)

