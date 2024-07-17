'''
- 번호 : 08979
- 제목 : 올림픽
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]

# 자료구조: (국가번호[0], 금[1], 은[2], 동[3])
A.sort(key = lambda x: (-x[1], -x[2], -x[3]))

# 자기 자신과 다른 Tuple이 나올 때까지 이전 탐색
def trace_back(idx:int, data:tuple) -> int:
    global A
    if idx < 0:
        return (idx + 1)
        
    if A[idx][1:4] == data[1:4]:
        return trace_back(idx-1, A[idx])
    else:
        return (idx + 1)

for i, data in enumerate(A):
    if data[0] == K:
        print(trace_back(i, data) + 1)
        break