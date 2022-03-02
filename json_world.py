import json

# JSON string
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'

employee_dict = json.loads(employee)
print(employee_dict, type(employee_dict))
print("\n")

employee_string = json.dumps(employee_dict, indent=4)
print(employee_string)

# list conversion to Array
print(json.dumps(['Welcome', "to", "GeeksforGeeks"]))

# tuple conversion to Array
print(json.dumps(("Welcome", "to", "GeeksforGeeks")))

with open("Sample.json", "w") as p:
    json.dump(employee_dict, p, indent=4)  # takes the object to dump and the destination to dump

with open("Sample.json", "r") as read_it:
    data = json.load(read_it)
    print(data)
