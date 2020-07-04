iterator = int(input(range(1, 21)))
odd_value = 0
output = 0
number = 0
    
for output in range(iterator) :
    for odd_value in range(iterator) :
        if odd_value % 2 != 0 :
            output = odd_value + output
            print( output )