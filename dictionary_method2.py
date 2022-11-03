# Dictionary
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
print('basket' in user)
print('age' in user.keys())
print('hello' in user.values())

# user.popitem()
# print(user)
user.update({'age': 55})
print(user)