# EXAMPLE 1: ZERO DIVIDER ERROR MESSAGE
def a():
    print('start of a()')
    b()  # call b()


def b():
    print('start of b()')
    c()  # call c()


def c():
    print('start of c()')
    42 / 0  # This will cause  a zero divider error


a()  # call a()







