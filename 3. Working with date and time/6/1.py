import time


def calculate_it(func, *args):
    start_time = time.perf_counter()
    answer = func(*args)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return answer, elapsed_time


def add(a, b, c):
    time.sleep(3)
    return a + b + c


result = calculate_it(add, 1, 2, 3)
print(result)