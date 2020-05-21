#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the introTutorial function below.
def introTutorial(V, arr):
    left = 0
    right = len(arr)-1
    mid = 0
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == V:
            return mid
        if arr[mid] > V:
            right = mid - 1
            
        if arr[mid] < V:
            left = mid + 1 
    return mid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
