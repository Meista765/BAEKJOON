import sys
input = sys.stdin.readline

import math

N = int(input())
P = [True] * 1e+9  # 소수

def Eratos(digit):
    for i in range(2, math.sqrt(10 ** digit) + 1):
        if P[i] == True:
            while i < 10 ** digit:
                
