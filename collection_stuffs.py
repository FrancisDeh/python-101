from collections import Counter, OrderedDict, defaultdict, ChainMap, namedtuple, deque, UserDict, UserList

# working with counter
count = Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C'])
print(count)

# with dictionary
print(Counter({'A': 3, 'B': 5, 'C': 2}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))

od = OrderedDict()  # remembers the order of keys even after deleting etc
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}


# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"


# Defining the dict
d = defaultdict(def_value)  # d = defaultdict(lambda: "Not Present") d = defaultdict(int) -- list etc
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])

# Defining the chainmap - creates a list of multiple dictionaries
c = ChainMap(d1, d2, d3)

print(c)
# c.values(), c.keys(), c.new_child(d4)

# named tuple, give name to keys
student = namedtuple('student', ['name', 'age', 'location'])
s1 = student("Francis Deh", 25, "Accra")
print(s1[1], s1.name)  # call by name
# use _make to get a named tuple from a list
s2 = student._make(["James Doe", 34, "Unknown"])
# asDict returns an ordered dictionary
s2_dict = s2._asdict()
print(s2_dict)

# deque - list optimized for append and pop
# Declaring deque
queue = deque(['name', 'age', 'DOB'])
print(queue)
queue.append("location")
queue.appendleft("number")
print(queue)
queue.pop()
queue.popleft()
print(queue)


# Creating a Dictionary where
# deletion is not allowed
class MyDict(UserDict):

    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # dictionary
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop popitem
    # from Dictionary
    def popitem(self, s=None):
        raise RuntimeError("Deletion not allowed")


# user_dict = UserDict()
# user_dict.data

# Driver's code
d = MyDict({'a': 1, 'b': 2, 'c': 3})


# d.pop(1)  # deletion is not allowed


# Creating a List where
# deletion is not allowed
class MyList(UserList):

    # Function to stop deletion
    # from List
    def remove(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # List
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")


# Driver's code
L = MyList([1, 2, 3, 4])

print("Original List")

# Inserting to List
L.append(5)
print("After Insertion")
print(L)

# Deleting From List
# L.remove() # not allowed
