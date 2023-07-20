#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here s- squares d-day m-month
    numbers = s
    target = d
    count = m
    
    result = 0
    
    if len(numbers) < count:
        return result
    
    part_sum = sum(numbers[:count])
    
    if part_sum == target:
        result += 1
        
    for i in range (1, len(numbers) - count + 1):
        part_sum = part_sum - numbers[i - 1] + numbers[i + count -1]
        if part_sum == target:
            result += 1
    return(result)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
