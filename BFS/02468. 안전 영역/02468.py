import sys
input = sys.stdin.readline

from collections import deque

def BFS(start_r, start_c, rainfall):
    queue = deque()
    
    visited[start_r][start_c] = 1
    queue.append((start_r, start_c))
    
    while queue:
        pos_r, pos_c = queue.popleft()
        
        # →, ↓, ↑, ←
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = pos_r + dr
            new_c = pos_c + dc
            
            if 0 <= new_r < N and 0 <= new_c < N and not visited[new_r][new_c] and buildings[new_r][new_c] > rainfall:
                visited[new_r][new_c] = 1
                queue.append((new_r, new_c))

def find_safe_area(rainfall):
    # 안전영역 개수
    cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and buildings[r][c] > rainfall:
                BFS(r, c, rainfall)
                cnt += 1
    
    return cnt

N = int(input())

# 입력 받기 및 최대 높이 경신
max_height = 0
buildings = [[] for _ in range(N)]
for idx in range(N):
    row = list(map(int, input().split()))
    max_height = max(max_height, *row)
    buildings[idx] = row


max_cnt = float('-inf')
for rainfall in range(max_height):  # (최대 높이 - 1)까지 탐색
    # 방문 리스트 초기화
    visited = [[0] * N for _ in range(N)]
    max_cnt = max(max_cnt, find_safe_area(rainfall))

print(max_cnt)