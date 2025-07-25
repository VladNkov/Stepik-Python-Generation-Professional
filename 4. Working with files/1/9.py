# Гуру прогрессий 🌶️
# Дана последовательность целых чисел. Напишите программу, которая определяет, является ли данная последовательность
# прогрессией, и если да, то определяет её вид.
# На вход программе подается произвольное количество строк (не менее трёх), в каждой строке записано натуральное
# число — очередной член последовательности.
# Программа должна вывести текст:
# Арифметическая прогрессия, если введенная последовательность чисел является арифметической прогрессией
# Геометрическая прогрессия, если введенная последовательность чисел является геометрической прогрессией
# Не прогрессия, если введенная последовательность чисел не является прогрессией
# Примечание 1. Гарантируется, что вид прогрессии определяется однозначно.

import sys


def is_arithmetic_progression(temp):
        diff = temp[1] - temp[0]
        return all(temp[i+1] - temp[i] == diff for i in range(len(temp)-1))


def is_geometric_progression(temp):
        ratio = temp[1]/temp[0]
        return all(temp[i+1]/temp[i] == ratio for i in range(len(temp)-1))


temp = list(map(int, sys.stdin.read().split()))
result1 = is_arithmetic_progression(temp)
result2 = is_geometric_progression(temp)
if result1:
        print('Арифметическая прогрессия')
elif result2:
        print('Геометрическая прогрессия')
else:
        print('Не прогрессия')

# Sample Input 1:
# 1
# 2. Data type set and dict.txt
# 3.txt
# 4. Data type namedtuple
# 5

# Sample Input 2. Data type set and dict.txt:
# 2. Data type set and dict.txt
# 4. Data type namedtuple
# 8
# 16

# Sample Input 3.txt:
# 1
# 9
# 1
# 1
# 4. Data type namedtuple
# 5