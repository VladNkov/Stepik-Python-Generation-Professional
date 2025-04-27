import time


def calculate_it(func, args):
    start_time = time.perf_counter()
    func(args)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time


def get_the_fastest_func(funcs, arg):
    fastest_func = min(funcs, key=lambda func: calculate_it(func, arg))
    return fastest_func


def slow(arg):
    time.sleep(3)


def fast(arg):
    time.sleep(1)


funcs = [slow, fast]
print(get_the_fastest_func(funcs, 1))