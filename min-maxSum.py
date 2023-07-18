#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total_sum = 0
    min_num = float('inf')
    max_num = float('-inf')

    for num in arr:
        total_sum += num
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    min_sum = total_sum - max_num
    max_sum = total_sum - min_num

    print(min_sum, max_sum)




    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
