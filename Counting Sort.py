#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    # Write your code here
    counter = [0] * 100 
    for i in range(len(arr)):
        counter[arr[i]] += 1
    return counter

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(' '.join(map(str, result)))
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
