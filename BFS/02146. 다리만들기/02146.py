import sys; input = sys.stdin.readline
from collections import deque

# DEBUG = True
DEBUG = False

def label_island(start_r, start_c, label):
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

def find_min_bridge():
    min_bridge = float('inf')
    
    for label in range(1, max(max(row) for row in arr) + 1):
        # 1. 각 라벨 별로 큐 만들기; 자료구조 = [행 좌표, 열 좌표, 최소 다리 길이]
        queue = deque()
        
        # 2. 각 섬의 테두리 찾기
        for r in range(N):
            for c in range(N):
                # arr(r, c)가 탐색하는 label이고
                if arr[r][c] == label:
                    # 4방향 중 바다(0)가 있다면
                    # ↓, →, ↑, ←
                    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                            queue.append((r, c, 0))
                            break
        
        # 3. 해당 테두리에서 다른 섬을 찾을때까지 BFS
        visited = [[0] * N for _ in range(N)]
        found = False
        
        while queue and not found:
            r, c, dist = queue.popleft()
            
            # ↓, →, ↑, ←
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr = r + dr
                nc = c + dc
                
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    # 탐색한 방향이 바다라면 큐에 추가
                    if arr[nr][nc] == 0:
                        visited[nr][nc] = dist + 1
                        queue.append((nr, nc, dist + 1))
                    # 탐색한 방향이 다른 섬이라면 최소 경로 갱신 후 탐색 종료
                    elif arr[nr][nc] != label:
                        min_bridge = min(min_bridge, dist)
                        found = True
                        break
        
        if DEBUG:
            print(f'{label}번 섬에서 다리를 건설할 때 확산 경향')
            for row in visited:
                print(*row)
            print()
    
    return min_bridge

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

if DEBUG:
    print()
    print('섬 구분 후 배열 형상')
    for row in arr:
        print(*row)
    print()

# 2. 다리 놓기
result = find_min_bridge()

# 3. 결과 출력
print(result)