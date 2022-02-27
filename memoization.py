# normal factorial
def factorial(x): return 1 if x == 1 else x * factorial(x - 1)


print(factorial(45))

# improving this using memoization and decorators
memory = {}


def memoize_factorial(func):
    def memoize(num):
        if num not in memory:
            memory[num] = func(num)
        return memory[num]

    return memoize


@memoize_factorial
def new_factorial(num): return 1 if num == 1 else num * new_factorial(num - 1)
print(new_factorial(45))