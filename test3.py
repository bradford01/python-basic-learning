# map
def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, [1, 2, 3])))


# Filter
def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, [1, 2,3])))


def a_in_usernames(item):
    return "a" in item.lower()


print(list(filter(a_in_usernames, ["JOHN", "ABRAHAM","KINGSLEY"])))


# zip
my_list = [1, 2, 3]
your_list = [10, 20, 30]
print(list(zip(my_list, your_list)))

# reduce
from functools import reduce


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, [1, 2, 3, 4, 5], 0))

# def accumulator_2(acc, item):
#     return lambda acc, use: acc + use
#
print(reduce(lambda acc, item: acc + item, [1, 2, 3], 5))