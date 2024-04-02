#!/bin/python3
# HLAWR was here!

import math
import os
import random
import re
import sys



def insertionSort1(n, arr):
    # Write your code here
    key = arr[n-1]
    j = n - 2
    while (j >= 0 and key < arr[j]):
        arr[j + 1] = arr[j]
        print(*arr)
        j -= 1
    arr[j + 1] = key
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
