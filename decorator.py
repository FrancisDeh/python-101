import time
import math


def calculate_time(func):
    def inner_calculate(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("total time taken in ", func.__name__, end - begin)

    return inner_calculate


@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))


factorial(10)


def irmer_it(func):
    def inner_irmer(*args, **kwargs):
        print("Before execution")
        returned_values = func(*args, **kwargs)
        print("After execution")
        return returned_values

    return inner_irmer


# irmer_it(sum_them(a, b))
@irmer_it  # decorators can be chained as well
def sum_them(x, y):
    print("inside the function")
    return x + y


a, b = 1, 2
print("Sum = ", sum_them(a, b))
