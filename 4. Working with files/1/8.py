# Это точно Python? 🌶️
# Дана последовательность дат. Напишите программу, которая определяет, в каком порядке расположены даты в данной
# последовательности.
# На вход программе подается произвольное количество строк (две или более), в каждой строке записана дата
# в формате DD.MM.YYYY.
# Программа должны вывести текст:
# ASC, если даты в введенной последовательности расположены строго в порядке возрастания
# DESC, если даты в введенной последовательности расположены строго в порядке убывания
# MIX, если даты в введенной последовательности расположены ни в порядке возрастания, ни в порядке убывания
# Параметры ASC и DESC используются в языке SQL для сортировки по возрастанию и по убыванию соответственно.

import sys
from datetime import datetime

temp = sys.stdin.read().split()
date_list = [datetime.strptime(date, '%d.%m.%Y').date() for date in temp]

asc_temp = sorted(date_list)
desc_temp = sorted(date_list, reverse=True)

if date_list == asc_temp and len(date_list) == len(set(date_list)):
    print('ASC')
if date_list == desc_temp and len(date_list) == len(set(date_list)):
    print('DESC')
if date_list != asc_temp and date_list != desc_temp or len(date_list) != len(set(date_list)):
    print('MIX')



# https://github.com/python-generation/Professional/blob/main/Module_4/Module_4.1/Module_4.1.17/input.txt
# https://github.com/python-generation/Professional/blob/main/Module_4/Module_4.1/Module_4.1.17/output.txt