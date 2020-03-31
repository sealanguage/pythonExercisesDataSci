n = int(input(range(1, 21)))
odd_value = 1
output = 0
number = 0
i = 0
    
for i in range(0, n) :
    output = odd_value + output
    print( "output is: ", output )
    odd_value = odd_value + 2