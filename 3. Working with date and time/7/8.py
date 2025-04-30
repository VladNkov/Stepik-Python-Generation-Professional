# ТЧМ
# Во многих музеях существует один день месяца, когда посещение музея для всех лиц или отдельных категорий граждан
# происходит без взимания платы. Например, в Эрмитаже это третий четверг месяца.
# Напишите программу, которая определяет даты бесплатных дней посещения Эрмитажа в заданном году.
# На вход программе подается натуральное число, представляющее год.
# Программа должна определить все даты бесплатных дней посещения Эрмитажа в введенном году и вывести их.
# Даты должны быть расположены в порядке возрастания, каждая на отдельной строке, в формате DD.MM.YYYY.


import calendar
from datetime import date


def get_all_thursdays(year):
    thursdays_list = []

    for month in range(1, 13):
        for week in calendar.monthcalendar(year, month):
            thursday = week[3]
            if thursday:
                thursdays_list.append(date(year, month, thursday))

    return thursdays_list


year = int(input())
result = get_all_thursdays(year)
month_dict = {}
for date in result:
    key = (date.year, date.month)
    if key not in month_dict:
        month_dict[key] = []
    month_dict[key].append(date)
third_thursday = []
for key, days in month_dict.items():
    third_thursday.append(days[2])
for i in third_thursday:
    print(i.strftime('%d.%m.%Y'))

