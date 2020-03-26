first = int(input("enter 1st num in range > "))
last = int(input("enter last num in range >"))
found_prime = True

for number in range (first, last) :
    for i in range(2, int((number)/2)+1) :
        print("number ", number, " is not prime")
        found_prime = False
        break
    if found_prime == True :
        print("number ", number, " is prime")
        found_prime = True