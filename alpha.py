import operator
import array as arr

# any - if any is true
print(any([True, False, False, True]))

# all - if all is true
print(all([True, False, False, True]))

# operator - div, mul etc, getitem, delitem, concat, contains
print(operator.truediv(4, 5))
li = [1, 2, 5, 8]
operator.setitem(li, 3, 6)  # set 6 to position 3 in the li list
print(li)
li.extend([98, 34])  # remove, pop(), pop(index)
print(operator.concat("Hello", "World"))

# nb. == is different from is.
w = "php artisan inspire"
# 3rd and 2nd last character
print(w[3:-2])
# formatting
s1 = "{} {} {}".format('Geeks', 'For', 'Life')
s2 = "{0} {1} {2}".format('Geeks', 'For', 'Life')
s3 = "{g} {f} {l}".format(g='Geeks', f='For', l='Life')
print(s1, s2, s3, sep=" * ")

# list slicing
# [::-index] - reverse
# [index:], [:index], [:], [index:index], [index:-index], [:-index]
print(li[::-1])

# tuples
x, y = (4, 5)
# set
s = set(li)
s.add(1)
s.update([123, 45, 67])
# s.discard(3) - does not throw KeyError s.remove(4) - throws KeyError if does not exist
# s.pop(), s.clear()
print(s)
print(frozenset())  # is immutable
# dict
hey = {}  # or dict()
a = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
b = dict([(1, 'Geeks'), (2, 'For')])
# b.popitem(), clear() del .get()

# arrays
h = arr.array('i', [1, 2, 3])  # 'd'
h.insert(1, 56)  # h.append(4)
h.remove(1)  # removes first occurrence of 1
h.pop(2)  # removes element at index 2
print(h)
