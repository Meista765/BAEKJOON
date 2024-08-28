import sys; input = sys.stdin.readline
from collections import deque

def label_island(start_r, start_c, label):
    global N, arr, visited
    
    queue = deque()
    
    visited[start_r][start_c] = 1
    queue.append((start_r, start_c))
    
    while queue:
        pos_r, pos_c = queue.pop()
        arr[pos_r][pos_c] = label
        
        # ↓, →, ↑, ←
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = pos_r + dr
            new_c = pos_c + dc
            if 0 <= new_r < N and 0 <= new_c < N and visited[new_r][new_c] == 0 and arr[new_r][new_c] == 1:
                visited[new_r][new_c] = 1
                queue.append((new_r, new_c))

# main
# 0. 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 섬 구분하기
visited = [[0 for _ in range(N)] for _ in range(N)]
label = 1
for r in range(N):
    for c in range(N):
        if not visited[r][c] and arr[r][c] == 1:
            label_island(r, c, label)
            label += 1

for row in arr:
    print(*row)
    
# 2. 각 섬의 테두리 찾기

# 3. 다리 놓기