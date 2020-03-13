prev_number = 0
next_number = 1
count = 0

while count < 10 :
    print(prev_number, end = " ")
    next = prev_number + next_number 
    prev_number = next_number
    next_number = next
    count = count + 1