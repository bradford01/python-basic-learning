# dictionary method
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
print(user.get('age'))
print(user.get('age', 65))  # this is saying if age does not exist in the dictionary insert it to have a value of 65


user2 = dict(name='JohnJohn')
print(user2)

