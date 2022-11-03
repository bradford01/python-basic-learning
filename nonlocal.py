def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)

    inner()
    print('outer:', x)


outer()

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple","papaya"]
thislist.extend(tropical)
print(thislist)
# The extend method does not have to append list, you can add any iterable object (tuples, sets, dictionaries etc.)
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist1 = ["apple", "banana", "cherry"]
print(thislist1)
# thislist1.remove("banana")
# print(thislist1)
# thislist1.pop(1)
# print(thislist1)
# thislist1.pop()
# print(thislist1)
# del thislist1
# thislist1.clear()
# print(thislist1)
for x in thislist1:
    print(x)

for i in range(len(thislist1)):
    print(thislist1[i])
