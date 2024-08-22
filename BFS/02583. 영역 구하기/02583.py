import sys
input = sys.stdin.readline

from collections import deque

len_r, len_c, repeat = map(int, input().split())

# 색칠 영역
A = [[0 for _ in range(len_c)] for _ in range(len_r)]

# 방문 리스트
visited = [[0 for _ in range(len_c)] for _ in range(len_r)]

# 영역 색칠하기
for _ in range(repeat):
    start_r, start_c, end_r, end_c = map(int, input().split())
    
    for pos_r in range(start_r, end_r):
        for pos_c in range(start_c, end_c):
            A[pos_r][pos_c] = 1

print("영역 색칠 후")
for row in A:
    print(*row)

queue = deque()
area = []
for pos_r in range(len_r):
    for pos_c in range(len_c):
        if A[pos_r][pos_c] == 0 and not visited[pos_r][pos_c]:
            visited[pos_r][pos_c] = 1
            queue.append((pos_r, pos_c))
            # 영역 구분하기(BFS): while-loop 1회당 영역 1개
            tmp_area = 0  # 영역의 넓이
            while queue:
                r, c = queue.popleft()
                
                A[r][c] = 2  # 방문 노드는 2로 변경
                tmp_area += 1  # 넓이 1 증가
                
                # ↓, →, ↑, ←
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < len_r and 0 <= nc < len_c and not visited[nr][nc] and A[nr][nc] == 0:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
            area.append(tmp_area)  # 넓이 추가

print("영역 구분 후")
for row in A:
    print(*row)

# 결과 출력
print(len(area))
print(*area)
