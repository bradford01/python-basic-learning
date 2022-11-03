print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33
if b > a:
    print('b is greater than a')
else:
    print('b is not greater than a')


# The bool() function allows you to evaluate any value, and give you True or False in return
print(bool('Hello'))
print(bool(15))
print(bool('abc'))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
x = 'Hello'
y = 15
print(bool(x))
print(bool(y))


class MyClass:
    def __len__(self):
        return 0


myobj = MyClass()
print(bool(myobj))


# function can return a boolean
def my_function():
    return True


print(my_function())
if my_function():
    print('yes')
else:
    print('NO!')

b = 200
print(isinstance(b, int))



