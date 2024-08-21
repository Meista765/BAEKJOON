import sys
input = sys.stdin.readline

from collections import deque

# enum
UNRIPEN = 0
RIPEN = 1
NULL = -1

def BFS():
    # 너비 우선 탐색
    max_day = 0  # 최소 일수 (max라 적은 이유는 배열에서의 최대가 곧 최소이므로)
    while queue:
        pos_r, pos_c = queue.popleft()
        
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = pos_r + dr
            new_c = pos_c + dc
            # index 범위 확인
            if 0 <= new_r < len_r and 0 <= new_c < len_c and not visited[new_r][new_c]:
                # 안 익은 토마토가 인접해 있다면
                if tomato[new_r][new_c] == UNRIPEN:
                    visited[new_r][new_c] = 1                       # 방문 리스트 체크
                    tomato[new_r][new_c] = tomato[pos_r][pos_c] + 1 # 토마토가 익기까지 걸린 일수를 저장
                    max_day = max(max_day, tomato[new_r][new_c])    # 최소 일수 경신
                    queue.append((new_r, new_c))                    # 다음 작업 구역 추가

    # 안 익은 토마토가 있으면 -1 출력, 그 외에는 최소 일수 출력
    for r in range(len_r):
        for c in range(len_c):
            if tomato[r][c] == UNRIPEN:
                print(-1)
                return
    
    print(max_day - 1)

len_c, len_r = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(len_r)]

# 방문 리스트 초기화
visited = [[0 for _ in range(len_c)] for _ in range(len_r)]

queue = deque()

# 익은 토마토의 위치 전부 저장
for r in range(len_r):
    for c in range(len_c):
        if tomato[r][c] == RIPEN:
            visited[r][c] = 1
            queue.append((r, c))

BFS()
