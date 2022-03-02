import math

"""
1. Consider the loop from Section 8.3 of your textbook.
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
     print(letter + suffix)
Put this code into a Python script and run it. Notice that it prints the names "Oack" and "Qack".
Modify the program so that it prints "Ouack" and "Quack" but leaves the other names
the same.
Include the modified Python code and the output in your submission.
"""
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    add_u = 'u' if letter == 'O' or letter == 'Q' else ''
    print(letter + add_u + suffix)
"""
Jack
Kack
Lack
Mack
Nack
Ouack
Pack
Quack
"""

"""
2. Give at least three examples that show different features of string slices. 
Describe the feature illustrated by each example. Invent your own examples. 
Do not copy them for the textbook or any other source.
"""

u = "always inspire"
# 3rd and 2nd last character
print(u[3:-2])

v = "have hope"
# reverse string
print(v[::-1])

w = "live and love"
# first 3 characters
print(w[:3])

"""
Part 1
Encapsulate the following Python code from Section 7.5 in a function
named my_sqrt that takes a as a parameter, chooses a starting value for x, and returns an estimate of the square root of a.
while True:
 y = (x + a/x) / 2.0
 if y == x:
     break
 x=y

"""


def my_sqrt(a):
    x = 1
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
    return x


def test_sqrt():
    a = 1
    while a <= 25:
        custom_sqrt = my_sqrt(a)
        py_sqrt = math.sqrt(a)
        print("a = {a} | my_sqrt({a}) = {s} | math.sqrt({a}) = {ss} | diff = {d}".format(a=a, s=custom_sqrt, ss=py_sqrt,
                                                                                         d=custom_sqrt - py_sqrt))
        a += 1


test_sqrt()
