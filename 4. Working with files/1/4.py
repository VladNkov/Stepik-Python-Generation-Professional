# Урок статистики
# Дан список чисел, каждое из которых — рост очередного ученика онлайн-школы BEEGEEK. Напишите программу, которая
# определяет рост самого низкого и самого высокого учеников, а также средний рост среди всех учеников.
# Формат входных данных
# На вход программе подается произвольное количество строк, в каждой строке записано натуральное число — рост очередного
# ученика онлайн-школы BEEGEEK.
# Программа должна определить рост самого низкого и самого высокого учеников, а также средний рост среди всех учеников.
# Полученные результаты должны быть выведены в следующем формате:
# Рост самого низкого ученика: <рост самого низкого ученика>
# Рост самого высокого ученика: <рост самого высокого ученика>
# Средний рост: <средний рост среди всех учеников>
# Примечание 1. Если на вход программе ничего не подается, то она должна выводить текст нет учеников

import sys

temp = sys.stdin.read().split()
data = list(map(int, temp))
if len(temp) > 0:
    print(f'Рост самого низкого ученика: {min(data)}')
    print(f'Рост самого высокого ученика: {max(data)}')
    print(f'Средний рост: {sum(data)/len(data)}')
elif len(temp) == 0:
    print('нет учеников')

# Sample Input 1:
#
# 185
# 170
# 190
# 155
# 175
