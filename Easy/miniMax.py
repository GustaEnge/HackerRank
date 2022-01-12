#!/bin/python3

import sys
def Adding(arr):
    r1 = 0
    r2 = 0
    arr.sort()
    for i in range(len(arr)-1):
        r1 += arr[i]
    r2 = (r1+arr[4]) - arr[0]
    
    return str(r1)+" "+str(r2)
    
arr = list(map(int, input().strip().split(' ')))
print(Adding(arr))

