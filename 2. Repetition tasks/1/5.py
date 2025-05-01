# Функция convert()
# Реализуйте функцию convert(), которая принимает один аргумент:
# string — произвольная строка
# Функция должна возвращать строку string:
# полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
# полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
# полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
# Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.


def convert(input_string):
    count_lower = 0
    count_upper = 0
    for letter in input_string:
        if letter.islower():
            count_lower += 1
        if letter.isupper():
            count_upper += 1
    if count_lower >= count_upper:
        return input_string.lower()
    else:
        return input_string.upper()


print(convert('BEEgeek'))