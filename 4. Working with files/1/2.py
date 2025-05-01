# Размах данных
# Дана последовательность дат. Напишите программу, которая выводит количество дней между максимальной и минимальной
# датами данной последовательности.
# Формат входных данных
# На вход программе подается произвольное количество строк, в каждой строке записана дата в ISO формате (YYYY-MM-DD).
# Формат выходных данных
# Программа должна вывести единственное число — количество дней между максимальной и минимальной датами введенной
# последовательности.

import sys
from datetime import datetime, date

temp = sys.stdin.read().split()
# max_date = datetime.strptime(max(temp), '%Y-%m-%d')
# min_date = datetime.strptime(min(temp), '%Y-%m-%d')
# print((max_date-min_date).days)

answer = date.fromisoformat(max(temp)) - date.fromisoformat(min(temp))
print(answer.days)

