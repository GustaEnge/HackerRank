#!/bin/python3

import sys
def solve(n, s, d, m):
    cont = 0
    for i in range(n-m+1):
        sum1 = 0
        for j in range(i,i+m):
                sum1 += s[j]
        if sum1 == d:
            cont += 1
                      
        
    return cont            

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
