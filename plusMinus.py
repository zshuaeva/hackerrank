#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    length = len(arr)
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for i in arr:
        if i > 0:
            positive_count += 1
        elif i < 0:
            negative_count += 1
        else:
            zero_count += 1

    positive_ratio = positive_count / length
    negative_ratio = negative_count / length
    zero_ratio = zero_count / length

    print(round(positive_ratio, 6))
    print(round(negative_ratio, 6))
    print(round(zero_ratio, 6))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
