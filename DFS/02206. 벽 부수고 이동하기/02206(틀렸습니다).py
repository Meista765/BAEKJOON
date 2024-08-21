import sys
input = sys.stdin.readline

from collections import deque

# 행과 열의 크기 받기
len_r, len_c = map(int, input().split())

# 입력 받기
maze = [list(map(int, list(input().rstrip()))) for _ in range(len_r)]

# 방문 리스트 초기화 (len_r X len_c)
visited = [[0 for _ in range(len_c)] for _ in range(len_r)]

# 너비 우선 탐색
min_path = float('inf')
queue = deque()

# 큐 자료구조: [x좌표(int), y좌표(int), 경로의 길이(int), 벽 통과 여부(bool)]
queue.append([0, 0, 1, False])
visited[0][0] = 1

while queue:
    pos_r, pos_c, cur_path, wall_through = queue.popleft()
    
    # 목적지 도착시, 최단 거리 경신
    if pos_r == len_r - 1 and pos_c == len_c - 1:
        min_path = min(min_path, cur_path)
    
    # 이외의 경우
    else:
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = pos_r + dr
            new_c = pos_c + dc
            if 0 <= new_r < len_r and 0 <= new_c < len_c and not visited[new_r][new_c]:
                # 0이면 무조건 진행, wall-through에 변화 없음
                if maze[new_r][new_c] == 0:
                    visited[new_r][new_c] = 1
                    queue.append([new_r, new_c, cur_path + 1, wall_through])
                # 벽을 마주했을 때는
                else:  # maze[new_r][new_c] == 1:
                    # 벽을 부술 기회가 남아있다면 부수고 다음으로 진행
                    if not wall_through:
                        visited[new_r][new_c] = 1
                        queue.append([new_r, new_c, cur_path + 1, True])

# 최소 경로가 갱신되지 않았으면
if min_path == float("inf"):
    print(-1)
# 그 외에는
else:
    print(min_path)