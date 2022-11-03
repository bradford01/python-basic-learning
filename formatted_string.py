# formatted strings
name = 'johnny'
age = 55
print('hi ' + name + '.you are ' + str(age) + ' years old.')
print(f'hi {name}. you are {age} years old.')  # MOST PREFERRED WAY
print('hi {}. you are {} years old'.format(name, age))
print('hi {1}. you are {0} years old'.format(name, age))
print('hi {new_name}. you are {new_age} years old.'.format(new_name='sylvester', new_age=100))


