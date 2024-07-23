'''
- 번호 : 11003
- 제목 : 최솟값 찾기
- 알고리즘 분류 : 우선순위 큐, 덱
'''

import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
my_deque = deque()

for i in range(N):
    # while (my_deque IS NOT EMPTY) & (my_deque's left data's value > value to insert)
    while my_deque and my_deque[-1][0] > A[i]:
        # discard
        my_deque.pop()
    
    # add new value
    my_deque.append((A[i], i))
    
    # discard data out of window
    if my_deque[0][1] < i-L+1:
        my_deque.popleft()
    
    print(my_deque[0][0], end=' ')