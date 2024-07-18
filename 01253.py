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
    left = 0
    right = N - 1
    
    while left < right:
        if left == idx:
            left += 1
            continue
        if right == idx:
            right -= 1
            continue
        
        if A[left] + A[right] > K:
            right -= 1
        elif A[left] + A[right] < K:
            left += 1
        else: # A[left] + A[right] == K
            count += 1
            break

print(count)