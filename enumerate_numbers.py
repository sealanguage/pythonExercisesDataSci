numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index, number in enumerate(numbers):
    if (index + 1) % 3 != 0:
        print(index, number)
