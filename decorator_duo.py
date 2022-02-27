# decorators taking parameters

def irmer_it(*args, **kwargs):
    def irmer(func):
        print("Inside inner irmer")
        print("I like your ", kwargs['like'])
        func()

    return irmer


@irmer_it(like="boldness")
def what_i_like():
    print("yes, that's what i like")


def bambi_it(x, y):
    def bambi(func):
        def inner_bambi(*args, **kwargs):
            print("Sum of args ".format(x + y))
            func(*args, **kwargs)

        return inner_bambi

    return bambi


# bambi_it(3, 4)
def looking_for_bambi(*args):
    for el in args:
        print(el)


# another way of using decorators
bambi_it(2, 4)(looking_for_bambi)("Here", "I", "Am")


def pearl_it(data_type, message_one, message_two):
    print(message_one)

    def pearl(func):
        def inner_pearl(*args, **kwargs):
            if any([type(arg) == data_type for arg in args]):
                print(message_two)
                return func(*args, **kwargs)
            else:
                return "Invalid Inputs"

        return inner_pearl

    return pearl


@pearl_it(str, "Decorator of joining string", "And joining begins..")
def join_string(*args):
    st = ''
    for s in args:
        st += s
    return st


@pearl_it(int, "Decorator for summing int", "And summing begins..")
def sum_int(*args):
    sm = 0
    for arg in args:
        sm += arg
    return sm


print(join_string("Call", " me", " Pearl"))
print(sum_int(3, 4, 8))
