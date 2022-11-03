# strings are immutable but list are mutable which means the item can be changed in place
amazon_cart = ['notebooks',
               'pencils',
               'toys',
               'grapes'
               ]
amazon_cart[0] = 'laptops'
# new_cart = amazon_cart[0:3]
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)

# creating a copy of amazon_cart to new_cart
# new_cart = amazon_cart[:]
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)


# This just assigns amazon_cart to new_cart
new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

