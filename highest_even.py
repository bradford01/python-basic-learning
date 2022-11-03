def highest_even(li):
    empty = []
    for numbers in li:
        if numbers % 2 == 0:
            empty.append(numbers)
    return empty





print(highest_even([1, 3, 5, 8, 10, 85, 44, 80,84, 86]))