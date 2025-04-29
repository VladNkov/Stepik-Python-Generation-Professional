# Количество дней 😉
# Напишите программу, которая определяет количество дней в заданном месяце.
# На вход программе подаются год и порядковый номер месяца (начиная с 1), разделенные пробелом.
# Программа должна вывести единственное число — количество дней в введенном месяце.

import calendar, time, datetime
from datetime import datetime

data = datetime.strptime(input(), "%Y %m")
print(calendar.monthrange(data.year, data.month)[1])