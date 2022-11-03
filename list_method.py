basket = [1, 2, 3, 4, 5]
# adding
# basket.append(100)  # append add an item or object in place it does not give a value
# print(basket)


basket.insert(3, 100)  # at index 3 insert 100 and it also add the item in place and not give a value
print(basket)


basket.extend([500])
print(basket)


# removing
basket.pop()  # removes the last value of the list
print(basket)


nam = basket.pop(0)  # this removes value at index 0 and it returns a value
print(basket)
print(nam)


basket.remove(2)  # this removes the value 2
print(basket)


basket.clear()  # removes whatever is in the list
print(basket)
