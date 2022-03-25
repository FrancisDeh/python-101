import json


# Invert_dict function from learning journal unit
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def read_file():
    with open('input_file.txt', 'r') as file:
        content = file.readline()
        return json.loads(content)


def write_invert_dict_to_file(d):
    with open('output_file.txt', 'w') as file:
        json.dump(d, file)


dict_content = read_file()
dict_content_invert = invert_dict(dict_content)
write_invert_dict_to_file(dict_content_invert)

"""
Python dictionary in string format is similar to JSON (JavaScript Object Notation) format.
To get a dictionary representation, i use the inbuilt python json library to load the string content
after reading the string content of the input file. 
This gives a dictionary representation of the content. Given that it's a dictionary,
the content can be inverted and converted back to a string.
We achieve this by using the python json dump method specifying the output file.
Our content is now written to the output file and stored as a string.
"""