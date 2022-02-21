# enumerate - looping technique, print index and value
for key, value in enumerate(["The", "Big", "Bang", "Theory"]):
    print(f"Key {key} and Value {value}")

# zip - combine 2 similar containers (list-list, dict-dict)
questions = ['name', 'color', 'shape']
answers = ['apple', 'red', 'a sphere']
for question, answer in zip(questions, answers):
    print('What is your {0}? I am {1}.'.format(question, answer))

# python code to demonstrate working of items()
d = {"geeks": "for", "only": "geeks"}

# using items to print the dictionary key-value pair
for i, j in d.items():  # time-consuming and memory intensive
    print(i, j)

li = [1, 6, 9, 3, 4, 3, 1]
for value in sorted(set(li)):
    print(value)

for i in reversed(li):  # reverses list
    print(i)
