#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
    counter = 0

    n = int(input().strip())    #  user input int of max (or maybe exact) n number of space separated ints 

    s = list(map(int, input().rstrip().split()))    #  will get input as a list of numbers from the user

    dm = input().rstrip().split()   #  get date and month - 2 user input ints 1-31, 1-12

    d = int(dm[0])    #  Ron's birthday or the goal number at 0 index

    m = int(dm[1])  #  Ron't birth month or range of numbers to add to get the goal number at 1 index

    result = birthday(s, d, m)   #  I'm not sure what it's doing, collects the values s, the goal d, the range m

    fptr.write(str(result) + '\n')   #  writing a string should be number of num combination that meets the ???

    fptr.close()