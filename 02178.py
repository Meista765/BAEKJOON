import sys
input = sys.stdin.readline

from collections import deque

def find_path(pos_x, pos_y):
    global min_path
    queue = deque()
    
    visited[pos_x][pos_y] = 1
    # 데이터 구조: (i, j, curr_len)
    queue.append((pos_x, pos_y, 1))
    
    while queue:
        now = queue.popleft()
        
        # 목적지 도착 시, 최소 경로 여부 확인 후 갱신
        if now[0] == N-1 and now[1] == M-1:
            if now[2] < min_path:
                min_path = now[2]
        else:
            for di, dj in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                ni = now[0] + di
                nj = now[1] + dj
                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and maze[ni][nj]:
                    visited[ni][nj] = 1
                    queue.append((ni, nj, now[2] + 1))


N, M = map(int, input().split())

# 미로
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]

# 방문 리스트
visited = [[0 for _ in range(M)] for _ in range(N)]

# 최소 길이
min_path = float('inf')

# 작업
find_path(0, 0)

# 출력
print(min_path)
