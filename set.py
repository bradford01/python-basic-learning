my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
"""
.difference()
.ddiscard()
.difference_update()
.intersection()
.isdisjoint()
.issubset()
issuperset()
.union()

"""
# print(my_set.difference(your_set))

# print(my_set.discard(5))
# print(my_set)

# print(my_set.difference_update(your_set))
# print(my_set)


print(my_set.intersection(your_set))

print(my_set.isdisjoint(your_set))  # it is asking if there is nothing in common and it output in booleans either true or false


print(my_set.union(your_set))
"""
instead of union you use this:
print(my_set | your_set)
"""
print(my_set.issubset(your_set))
print(your_set.issuperset(my_set))
