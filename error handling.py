# Error handling
# while True:
#     try:
#         age = int(input("what is your age"))
#         10 / age
#
#     except ValueError:
#         print("please type in a number or integer")
#
#     except ZeroDivisionError:
#         print("number must be integer except from 0")
#
#     else:
#         print("Thank you")
#         break
#

def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError)as err:
        print("oooppps")



print(sum(2, 0))

