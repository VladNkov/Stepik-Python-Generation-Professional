from math import factorial
import time


def for_and_append():  # с использованием цикла for и метода append()
    start_time = time.perf_counter()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    end_time = time.perf_counter()
    elapsed_time1 = end_time - start_time
    return elapsed_time1


def list_comprehension():
    start_time = time.perf_counter()
    iterations = 10_000_000
    answer = [i + 1 for i in range(iterations)]
    end_time = time.perf_counter()
    elapsed_time2 = end_time - start_time
    return elapsed_time2


def calculate_it(func, *args):
    start_time = time.perf_counter()
    answer = func(*args)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return answer, elapsed_time


print(for_and_append())
print(list_comprehension())