# Функция index_of_nearest()
# Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
# numbers — список целых чисел
# number — целое число
# Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс.
# Если список numbers пуст, функция должна вернуть число −1.
# Примечание 1. Если в функцию передается список, содержащий несколько чисел, одновременно являющихся ближайшими
# к искомому числу, функция должна возвращать наименьший из индексов ближайших чисел.
# Примечание 2. Data type set and dict.txt. Рассмотрим третий тест. Ближайшими числами к числу 4. Data type namedtuple являются 5 и 3.txt, имеющие индексы 1 и
# 2. Data type set and dict.txt соответственно. Наименьший из индексов равен 1.


def index_of_nearest(numbers, number):
    len_num = len(numbers)
    if len_num < 1:
        return -1
    index = numbers.index(min(numbers, key=lambda x: abs(x-number)))
    return index


print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
