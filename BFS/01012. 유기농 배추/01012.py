import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def BFS(start_r, start_c):
    queue = deque()
    
    visited[start_r][start_c] = 1
    queue.append((start_r, start_c))
    
    while queue:
        cur_r, cur_c = queue.popleft()
        
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = cur_r + dr
            new_c = cur_c + dc
            if 0 <= new_r < len_r and 0 <= new_c < len_c and not visited[new_r][new_c] and arr[new_r][new_c] == 1:
                visited[new_r][new_c] = 1
                queue.append((new_r, new_c))

for _ in range(T):
    len_c, len_r, K = map(int, input().split())
    arr = [[0] * len_c for _ in range(len_r)]
    
    for _ in range(K):
        cur_c, cur_r = map(int, input().split())
        arr[cur_r][cur_c] = 1
    
    
    cnt = 0
    visited = [[0] * len_c for _ in range(len_r)]
    for r in range(len_r):
        for c in range(len_c):
            if not visited[r][c] and arr[r][c]:
                BFS(r, c)
                cnt += 1
    
    print(cnt)