def hello():
    print("hellooooo")


greet = hello

print(greet())


def helloo(func):
    func()


def greete():
    print("i'm here")


a = helloo(greete)
print(a)


# higher order function
def big_boy(func):
    func()


def my_decorator(func):
    def wrap_func(x):
        print("*******")
        func(x)
        print("*******")

    return wrap_func


# @my_decorator
# def hello1():
#     print("helloooo")

@my_decorator
def hello1(greeting):
    print(greeting)

hello1("hiiiii")


# @my_decorator
# def bye():
#     print("see you later")
#
# bye()