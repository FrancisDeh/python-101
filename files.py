# Python code to illustrate split() function
# Python code to illustrate split() function
with open("file.text", "w") as file:
    file.write("Something to write")

with open("file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
