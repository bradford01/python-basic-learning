thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': '1964',
    'year': '2020',
    'colors': ['red', 'white', 'blue']
}
print(thisdict['colors'][0])
print(thisdict['brand'])
print(thisdict.get('brand'))
print(thisdict.keys())
thisdict['colours'] = 'yellow'
print(thisdict.keys())
print(thisdict.values())

this_dict1 = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
if 'model' in this_dict1:
    print('yes, \'model\' is one of the keys in thisdict dictionary')


this_dict1.update({'year': 2020})
print(this_dict1)


# removing items
this_dict2 = {'tools': 'local', 'name': 'master', 'date': 1962, 'color': 'red'}
# this_dict2.pop('name')
# print(this_dict2)
# this_dict2.popitem()  # this removes the last inserted item
# print(this_dict2)
# del this_dict2['name']
# print(this_dict2)
# del this_dict2
# print(this_dict2)
this_dict2.clear()
print(this_dict2)


