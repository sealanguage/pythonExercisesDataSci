import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    If  is odd, print Weird/
    if(n %2 != 0) :
        print("Weird")

#     If  is even and in the inclusive range of 2 to 5, print Not Weird
    if(n %2 != 0 and n > 1 ) :
        print("Not Weird")
     
#     If  is even and in the inclusive range of  to , print Weird
    if(n %2 == 0 and 6 <= n and n >= 20) :
        print("Weird")
        
        
#     If  is even and greater than , print Not Weird    
    if(n %2 == 0 and n > 20) :
        print("Not Weird")