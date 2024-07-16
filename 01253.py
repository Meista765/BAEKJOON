'''
- 번호 : 1253
- 제목 : 좋다
- 핵심 : Two-pointers
'''

import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
A.sort()

count = 0
for idx, K in enumerate(A):
    i = 0
    j = idx - 1
    
    while i < j:
        if A[i] + A[j] > K:
            j -= 1
        elif A[i] + A[j] < K:
            i += 1
        else:
            count += 1
            break

print(count)