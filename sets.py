thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

print("\n")
thisset1 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset1.update(tropical)
print(thisset1)

print("\n")
thisset2 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset2.update(mylist)
print(thisset2)


# to remove an item use the remove method or discard
thisset3 = {"apple", "banana", "cherry"}
# thisset3.remove("banana")
# thisset3.discard("banana")
x = thisset3.pop()
print(x)
print(thisset3)

# Join two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set3 = {"a", "b", "c"}
set4 = {1, 2, 3}
set3.update(set4)
print(set3)


# intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# intersection will return a new set that only contains items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
print(x)

# symmetric_difference_update() method will only keep the elements that are not present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# symmetric_difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
