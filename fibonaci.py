prev_number = 0
next_number = 1
count = 10

# solution = prev_number + next_number 
# print("solution", solution)

for i in range(count) :
    print(prev_number, end = " ")
    next = prev_number + next_number 
    prev_number = next_number
    next_number = next

