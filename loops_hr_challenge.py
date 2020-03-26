n = int(input(range(1, 21)))
odd_value = n
output = 0
counter = 0

for odd_value in range(n) :
    if odd_value % 2 != 0 :
        output = odd_value + output
        print( output )