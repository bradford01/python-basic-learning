# square the list with lambda
my_list = [5, 4, 3]

print(list(map(lambda a: a ** 2, my_list)))
# list sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

(a.sort(key=lambda x: x[1]))
print(a)


simpledict = {
    "a": 1,
    "b": 2
}

my_dict = {k: v * 2 for k, v in simpledict.items()}
print(my_dict)

c =[3, 4, 6, 8, 9, 10]
d  = ["2" if a > 9 else "tw0" for a in c]
print(d)