name = input('please what is your name?')
password = input('please write a password before you can login?')
password_length = len(password)
hidden_password = '*' * password_length
print(f'hey {name}, your password {hidden_password} is {password_length} letters long')
