import sys

input = sys.stdin.readline

from collections import deque

DEBUG = True
# DEBUG = False

ROW, COL, T = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(ROW)]

upper_ac = None  # 공청기 상부 좌표
lower_ac = None  # 공청기 하부 좌표
# 미세먼지가 확산되기 위해서는 해당 칸에 최소 5개 이상의 미세먼지가 있어야 한다.
diffusion_lst = deque()  # 확산될 먼지의 좌표 리스트

for r in range(ROW):
    for c in range(COL):
        if ARR[r][c] == -1:  # (r, c)에 값이 존재하는 경우,
            upper_ac = (r, c)
            lower_ac = (r + 1, c)
            break

if DEBUG:
    print(f"공청기 상부 좌표: {upper_ac}")
    print(f"공청기 하부 좌표: {lower_ac}")
    print(f"작업 리스트: {diffusion_lst}")

# 확산
next_diffusion_lst = deque()
for r, c in diffusion_lst:
    diffuse = int(ARR[r][c] / 5)
    # ↓, →, ↑, ←
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr = r + dr
        nc = r + dc
        # 범위를 벗어나거나, 공청기에 가로막혀 있으면 확산 불가
        if nr < 0 or nr >= ROW or nc < 0 or nc >= COL or ARR[nr][nc] == -1:
            continue
        ARR[r][c] -= diffuse  # 기존 좌표에는 확산량을 빼고,
        ARR[nr][nc] += diffuse  # 새 좌표에는 확산량을 더한다
        if diffuse > 4:  # 확산량이 5 이상이면 다음 작업에 추가한다
            next_diffusion_lst.append((nr, nc))
    if ARR[r][c] > 4: # 확산 후, 남은 좌표도 5 이상이면 다음 작업에 추가
        next_diffusion_lst.append((r, c))
diffusion_lst = next_diffusion_lst


if DEBUG:
    print(f"작업 리스트: {diffusion_lst}")


# # 반시계방향: →, ↑, ←, ↓
# CCW = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# # 시계방향: →, ↓, ←, ↑
# CW = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# # 공기 순환
# for delta, r, c in [(CW, lower_ac), (CCW, upper_ac)]:
#     k = 0 # 델타를 변경하는 스위치(0 ~ 3)
#     c += 1 # 우측으로 1회 이동
#     tmp = ARR[r]