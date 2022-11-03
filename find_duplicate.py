some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

empty = []

i =0
for a in some_list:
    if some_list.count(a) > 1:
        if a not in empty:
            empty.append(a)


print(empty)
