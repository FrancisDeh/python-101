# def function_name(parameters):
#   """docstring"""
#    statement(s)
#   return expression

def area(r, pi=3.142):  # default arguments
    return pi * r ** 2


print(area(4))
print(area(4, 3.14))
"""
*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)
"""


def random_sentences(*words):  # args
    for word in words:
        print(word, end=" ")


def user_profile(**details):  # kwargs
    for key, detail in details.items():
        print(key, detail, sep=" -> ")


random_sentences("Hello", "Francis", "How", "are", "you?")
user_profile(name="Francis", age=12, location="Accra")


def modify_an_element(lsts):
    lsts[0] = 45


lst = [1, 2, 3, 4]
print("Original list", lst)
modify_an_element(lst)
print("Element list", lst)


def swap(x, y):
    temp = x
    x = y
    y = temp
    print(x, y)


x = 2
y = 3
swap(x, y)  # values are not modified
print(x)
print(y)


# lambda - anonymous functions
def cube(z): return z * z * z


cube_v2 = lambda z: z * z * z  # lambda x: x*x
print(cube_v2(34))


def take(arg1, arg2, arg3):
    print('arg1', arg1)
    print('arg2', arg2)
    print('arg3', arg3)


d = ("Jelly", "Fish", "Eats")
take(*d)
d2 = {"arg1": "James", "arg2": "Bond", "arg3": "Kills"}
take(**d2)


def simple_generator():  # returns the result as and when ready without storing to memory
    yield 1
    yield 2
    yield 3


for v in simple_generator():
    print("Generator", v)

# generator object
x = simple_generator()
print(x.__next__())

filtered = filter(lambda val: val > 4, [3, 4, 5, 6, 7])
print(list(filtered))
