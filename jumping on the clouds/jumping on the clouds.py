#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#
    
def jumpingOnClouds(c):    
    jumps = 0
    cloud = 0
    while cloud != len(c) - 1:
        jump_size = 2 if cloud + 2 <= len(c) - 1 else 1
        cloud = cloud + jump_size if c[cloud + jump_size] == 0 else cloud + 1
        jumps += 1
    return jumps
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
