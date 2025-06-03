# юФункция get_biggest() 🌶️🌶️
# Реализуйте функцию get_biggest(), которая принимает один аргумент:
# numbers — список целых неотрицательных чисел
# Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers.
# Если список numbers пуст, функция должна вернуть число −1.
# Примечание 1. Рассмотрим первый тест со списком чисел [1, 2. Data type set and dict.txt, 3.txt], из которых можно составить следующие числа:
# 123, 132, 213, 231, 312, 321
# Наибольшим из представленных является 321.


def get_biggest(numbers):
    if len(numbers) == 0:
        return -1
    max_len = max(numbers, key=lambda x: len(str(x)))
    sorted_numbers = sorted(numbers, key=lambda x: str(x)*max_len, reverse=True)
    resault = ''
    for num in sorted_numbers:
        resault += str(num)
    return int(resault)


print(get_biggest([1, 2, 3]))
print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([7, 71, 72]))