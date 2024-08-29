import sys; input = sys.stdin.readline
from collections import deque

def bfs_island_labeling_and_edges(N, arr):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[0] * N for _ in range(N)]
    label = 1
    edges = []

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1 and not visited[r][c]:
                queue = deque([(r, c)])
                visited[r][c] = 1
                arr[r][c] = label
                island_edges = []

                while queue:
                    cur_r, cur_c = queue.popleft()
                    is_edge = False

                    for dr, dc in directions:
                        nr, nc = cur_r + dr, cur_c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = 1
                                arr[nr][nc] = label
                                queue.append((nr, nc))
                            elif arr[nr][nc] == 0:
                                is_edge = True

                    if is_edge:
                        island_edges.append((cur_r, cur_c, 0))
                
                edges.append(island_edges)
                label += 1

    return edges

def find_min_bridge(N, arr, edges):
    min_bridge = float('inf')
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    for label, edge in enumerate(edges, start=1):
        visited = [[0] * N for _ in range(N)]
        queue = deque(edge)
        
        while queue:
            r, c, dist = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    if arr[nr][nc] == 0:
                        queue.append((nr, nc, dist + 1))
                    elif arr[nr][nc] != label:
                        min_bridge = min(min_bridge, dist)
                        break
    
    return min_bridge

# main
N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

edges = bfs_island_labeling_and_edges(N, arr)
result = find_min_bridge(N, arr, edges)

print(result)
