#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    bigger = 0
    cont = 0
    for i in range(n):
        if ar[i] > bigger :
            bigger = ar[i]
    for i in range(n):
        if ar[i] == bigger:
            cont +=1
    return cont 

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)

