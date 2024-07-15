'''
- 번호 : 1292
- 제목 : 쉽게 푸는 문제
- 핵심 : 수열의 합 (n-square)
'''

import sys
input = sys.stdin.readline

idx_arr = []
for i in range(46):
    idx = i * (i+1) // 2
    idx_arr.append(idx)

print(*idx_arr)