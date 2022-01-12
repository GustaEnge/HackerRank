#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    seaLevel = 0
    condValley = False
    qtd = 0
    for i in s:
        seaLevel = seaLevel + 1 if i == "U" else seaLevel - 1
        if seaLevel < 0:
            condValley = True
        elif seaLevel == 0  and condValley:
            qtd += 1     
            condValley = False
    return qtd 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
