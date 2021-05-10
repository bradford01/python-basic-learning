# fundamental data types
# int and float
# in order to comment the program, highlight the block and press ctrl + /
# print(type(2 + 4))
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2 / 4))
#
#
# print(type(0.00001))
# print(2 ** 2)  # this is  2 raise to power of 2
# print(3 // 4)  # this round the division to whole number
# print(5 // 4)
# print(5 % 4)  # this prints only the remainder of the division
# print(6 % 4)


# math function
print(round(3.1))
print(round(3.9))

# int
my_int = 6
print('value: {}, type:{}'.format(my_int, type(my_int)))


# float
my_float = float(my_int)
print('value: {}, type: {}'.format(my_float, type(my_float)))


# note that division of int produces float
print(1 / 1)
print(6 / 5)


val = 0.1 + 0.1 + 0.1
print(val == 0.3)
print(val)


from decimal import Decimal
from_float = Decimal(0.1)
from_str = Decimal('0.1')
print('from_float: {}\nfrom_string: {}'.format(from_float, from_str))


my_decimal = Decimal('0.1')
sum_of_decimal = my_decimal + my_decimal + my_decimal
print(sum_of_decimal == Decimal('0.3'))



