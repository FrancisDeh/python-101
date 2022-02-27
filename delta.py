import logging

logging.basicConfig(filename="example.log", level=logging.INFO)


def shout(text: str):
    return text.upper()


def execute(func):  # pass in a function
    print(func("Hello World"))


execute(shout)


def create_adder(x):
    def add(y):
        return x + y

    return add


add_15 = create_adder(3)
print(add_15(15))


def logger(func):
    def log_func(*args):
        logging.info("Running function {} with arguments {}".format(func.__name__, args))
        print(func(*args))

    return log_func


def add(x, y): return x + y


def minus(x, y): return x - y


adder_logger = logger(add)
minus_logger = logger(minus)
adder_logger(3, 4)
minus_logger(3, 4)
