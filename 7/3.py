# День недели
# Напишите программу, которая определяет день недели, соответствующий заданной дате.
#
# Формат входных данных
# На вход программе подается дата в формате YYYY-MM-DD.
#
# Формат выходных данных
# Программа должна вывести полное название дня недели на английском, который соответствует введенной дате.

import calendar, time, datetime
from datetime import datetime
days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
data = datetime.strptime(input(), "%Y-%m-%d")

# print(datetime.strftime(data, '%A'))
print(days.get(calendar.weekday(data.year, data.month, data.day)))