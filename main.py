import time
import io


# import antigravity  # 😄 fun to try - uncomment to see


def print_hi(name):
    print(f'Hi, {name}', end="**\n")
    print([x for x in range(12)])
    x, y = input("Enter two lucky numbers: ").split()
    print(f"{x} and {y}")
    z = list(map(int, input("Enter multiple values").split()))
    print(f"All values {z}")
    c = [int(v) for v in input("Enter many values: ").split()]
    d = [int(v) for v in input("Enter many values separated by comma: ").split(",")]
    print("Entering many values {} and {}".format(c, d))


def func():
    """ This is a multiline comment """
    age = 23
    tips = 1 if 20 > 45 else 0  # ternary in python
    print(f"tips {tips}")

    def func2():
        nonlocal age  # similar to global
        age = age + 45
        print(age)

    func2()


def flush_counter():
    count_seconds = 3
    for i in reversed(range(count_seconds + 1)):
        if i > 0:
            print(i, end=">>>", flush=True)
            time.sleep(1)
        else:
            print("Start")


def print_to_file():
    dummy_file = io.StringIO()
    print("This is the beginning of python greatness", file=dummy_file)
    print(dummy_file.getvalue())


def print_without_newline():
    hey = [x for x in reversed(range(5)) if x % 2 == 0]
    for i in hey:
        # print(i),  # depends on the version, 2.x
        print(i, end=" ")  # depends on the version, 3.x
    print("\nWithout loops")
    print(*hey)  # without using loops but on one line
    print("16", "09", "2022", sep="-")


class Yell:
    """ Demonstrating operator overloading """

    def __init__(self, msg):
        self.msg = msg

    def __add__(self, other):
        """ Add two yell classes """
        return self.msg + other.msg


def demonstrate_operator_overloading():
    yell1 = Yell("Heyyyy.. ")
    yell2 = Yell("Have you eaten?")
    print(yell1 + yell2)


class SoComplex:
    """ We will add two complex numbers """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        """ Add two complex classes """
        return self.a + other.a, self.b + other.b

    def __gt__(self, other):  # lt, eq etc
        """ Compare two complex classes """
        return self.a > other.a and self.b > other.b


def demonstrate_so_complex_add():
    complex1 = SoComplex(4, 5)
    complex2 = SoComplex(8, 0)
    print(complex1 + complex2)
    print(complex1 > complex2)


if __name__ == '__main__':
    # print_hi('PyCharm')
    # func()
    # print_to_file()
    # print_without_newline()
    # demonstrate_operator_overloading()
    demonstrate_so_complex_add()
