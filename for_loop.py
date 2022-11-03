for item in (1, 2, 3, 4, 5):
    print(item)


for item in (1, 2, 3, 4, 5):
    for x in ["a", "b", "c"]:
        print(item, x)


user = {
    "name": "Golem",
    "age": 5006,
    "can_swim": False
}

for items in user.values():
    print(items)


for items in user.items():
    print(items)

for items in user.items():
    key, values = items
    print(key, values)
