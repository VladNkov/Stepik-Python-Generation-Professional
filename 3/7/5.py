# Количество дней 😎
# Напишите программу, которая определяет количество дней в заданном месяце.
# На вход программе подаются год и полное название месяца на английском, разделенные пробелом.
# Программа должна вывести единственное число — количество дней в введенном месяце.

import calendar, time, datetime
from datetime import datetime

date = datetime.strptime(input(), "%Y %B")
print(calendar.monthrange(date.year, date.month))