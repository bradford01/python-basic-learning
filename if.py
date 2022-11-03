a = 200
b = 33
c = 500
if a > b: print("A is greater than B")
print(a) if a > b else print(b)
print(a) if a > b else print("==") if a == b else print(b)

# AND
if a > b and c > a :
    print("Both conditions are true")


if a > b or a > c:
     print("at least one of the condition is true")


# NESTED IF
x = 41
if x > 10:
     print("Above 10")
     if x > 20:
         print("And also above 20")

else:
    print("but not above 20")

