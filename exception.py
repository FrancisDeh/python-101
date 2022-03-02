try:
    value = 45 / 0
except ZeroDivisionError:
    print("oops")
else:
    print("No oops")

try:
    value = 45 / 0
except ZeroDivisionError:
    print("oops")
except FileNotFoundError:
    print("ooooopps")
finally:
    print("after all the  oops")


class NameErrorException(Exception):
    # def __init__(self, value):
    #     self.value = value
    #
    # def __str__(self):
    #     return repr(self.value)
    pass


def print_name(name: str):
    if len(name) > 1:
        print(name.lower())
    else:
        raise (NameErrorException("Name is not valid"))


try:
    print_name("a")
except NameErrorException:  # as exception
    print("caught")
