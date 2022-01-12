#!/bin/python3

import sys

def migratoryBirds(n, ar):
    new = []
    cont = 0
    cont2 = 0
    ar.sort()
    num = ar[0]
    great = 0
    
    for i in range(n):
        if ar[i] == num and i < n-1:
            cont += 1
        else:
            new.append([num,cont])
            num = ar[i]
            if cont > great:
                great = cont
            cont = 1
       
            
    for j in range(len(new)):
        if new[j][1] == great:
            return new[j][0]
            
               
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
