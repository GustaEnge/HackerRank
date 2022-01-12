#!/bin/python3

import sys

def Counting(s,t,a,b,m,n,apple,orange):
    posA = 0
    posB = 0
    comp = t - s
    contA = 0
    contB = 0
    for i in range(len(apple)):
        if apple[i] > 0:
            posA = a + apple[i]
            if s <= posA <= t:
                contA += 1
    for j in range(len(orange)):
        if orange[j] < 0:
            posB = b + orange[j]
            if  s <= posB <= t:
                contB += 1
    return str(contA)+"\n"+str(contB)


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
print(Counting(s,t,a,b,m,n,apple,orange))
