import sys;
input = sys.stdin.readline
from collections import deque

N = 5
A = [input().split() for _ in range(N)]

queue = deque()
answers = set()

# 초기설정
for r in range(N):
    for c in range(N):
        queue.append((r, c, A[r][c]))

# BFS
while queue:
    pos_r, pos_c, number = queue.popleft()
    
    if len(number) == 6:
        answers.add(number)
        continue
    
    # ↓, →, ↑, ←
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_r = pos_r + dr
        new_c = pos_c + dc
        if 0 <= new_r < N and 0 <= new_c < N:
            queue.append((new_r, new_c, number + A[new_r][new_c]))

# 결과 출력
print(len(answers))