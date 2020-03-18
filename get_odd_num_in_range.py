first_number = int(input("enter first number in range > "))
last_number = int(input("enter last number in range > "))
nth_odd_num  = int(input("enter the nth odd number > "))
count = 0  # count the odd numbers
actual_nth_odd_num = 0

for number in range(first_number, last_number + 1) :
    if number %2 != 0 :
        count = count + 1
        if count == nth_odd_num :
            actual_nth_odd_num = number
            break
                
print(number)
