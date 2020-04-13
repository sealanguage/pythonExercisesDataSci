odd_1 = [1, 3, 5]
odd_2 = [7, 9, 11]

odd_1.extend(odd_2)
odd_1.insert(4, 6)
print(odd_1)
odd_1[3] = 10
print(odd_1)
odd_1.pop()
print(odd_1)
odd_1.pop(3)
odd_1.clear()