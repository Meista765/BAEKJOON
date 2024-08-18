import sys
input = sys.stdin.readline

from collections import deque

# enum
ROW = 0
COL = 1

# BFS
def BFS():
    visited[start[ROW]][start[COL]] = 1
    queue.append((*start, 0))
    
    while queue:
        pos_r, pos_c, depth = queue.popleft()
        
        if pos_r == end[ROW] and pos_c == end[COL]:
            print(depth)
            return
        
        for dr, dc in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            new_r = pos_r + dr
            new_c = pos_c + dc
            if 0 <= new_r < N and 0 <= new_c < N and not visited[new_r][new_c]:
                visited[new_r][new_c] = 1
                queue.append((new_r, new_c, depth + 1))

# main #
T = int(input())
for _ in range(T):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    
    # BFS
    queue = deque()
    
    BFS()