fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# newlist = [x for x in fruits if x != "apple"]
# newlist = [x for x in fruits]
# newlist = [x for x in range(10)]
# newlist = [x for x in range(10) if x < 5]
# newlist = [x.upper() for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print("\n")
# sort descending
thislist.sort(reverse=True)
print(thislist)

thislist1 = [100, 50, 65, 82, 23]
thislist1.sort()
print(thislist1)
print("\n")
# sort descending
thislist1.sort(reverse=True)
print(thislist1)


# customize sort function
def myfunc(n):
    return abs(n - 50)

thislist2 =[100, 50, 65, 82, 23]
thislist2.sort(key=myfunc)
print(thislist2)


# case sensitive sort
thislist3 = ["banana", "Orange", "Kiwi", "cherry"]
# thislist3.sort()
# print(thislist3)
# thislist3.sort(key=str.lower)
# print(thislist3)
thislist3.sort(reverse=True)
print(thislist3)



