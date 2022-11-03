adj = ["red", "big ", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        pass
    print(x, y)


def my_function(*kids):
    print("the youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(country="Norway"):
    print(f"i am from {country}")

my_function("Sweden")
my_function("india")
my_function()

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)



x = lambda a: a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))


def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(11))