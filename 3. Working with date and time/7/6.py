# Функция get_days_in_month() Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем
# порядке: year — натуральное число month — полное название месяца на английском Функция должна возвращать
# отсортированный по возрастанию список всех дат (тип date) месяца month и года year. Примечание 1. Repetition tasks. Например,
# вызов: get_days_in_month(2021, 'December') должен вернуть список: [datetime.date(2021, 12, 1. Repetition tasks), datetime.date(2021,
# 12, 2), ..., datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]


import calendar
from datetime import date, timedelta


def get_days_in_month(year, month):
    month_number = list(calendar.month_name).index(month)

    month_days = calendar.monthrange(year, month_number)[1]
    days_list = [date(year, month_number, day) for day in range(1, month_days + 1)]
    return days_list


answer = get_days_in_month(2021, 'December')
print(answer)