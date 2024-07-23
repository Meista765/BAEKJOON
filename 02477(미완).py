'''
- 번호 : 
- 제목 : 
'''

from collections import deque

import sys
input = sys.stdin.readline

K = int(input) # 단위면적당 참외 개수
direction = deque() # 동(1), 서(2), 남(3), 북(4)
length = deque() # 길이 정보

# 변수 입력
for _ in range(6):
    d, l = map(int, input().split())
    direction.append(d)
    length.append(l)