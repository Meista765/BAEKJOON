import sys
imput = sys.stdin.readline

from collections import deque

def BFS():
    visited = [[0] * M for _ in range(N)]
    
    queue = deque()
    visited[0][0] = 1
    queue.append((0, 0, 0))
    
    while queue:
        cur_r, cur_c, break_wall = queue.popleft()
        
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = cur_r + dr
            new_c = cur_c + dc
            if 0 <= new_r < N and 0 <= new_c < M and not visited[new_r][new_c]:
                if not break_wall and maze[new_r][new_c] == 1:
                    queue.append((new_r, new_c, 1))
                elif maze[new_r][new_c] == 0:
                    queue.append((new_r, new_c, 0))
                    

N, M = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]