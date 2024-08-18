import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def is_NG(pos_r, pos_c):
    # ↖, ↗, ↙, ↘
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        new_r = pos_r + dr
        new_c = pos_c + dc
        while 0 <= new_r < N and 0 <= new_c < N:
            if bishop[new_r][new_c]:
                return True
            new_r += dr
            new_c += dc
    return False

max_cnt = 0
def DFS(idx, cur_cnt):
    global max_cnt
    if idx == max_depth:
        max_cnt = max(max_cnt, cur_cnt)
    else:
        pos_r, pos_c = need_to_fill[idx]
        # 놓을 수 있으면 놓고 다음 탐색
        if not is_NG(pos_r, pos_c):
            bishop[pos_r][pos_c] = 1
            DFS(idx + 1, cur_cnt + 1)
            bishop[pos_r][pos_c] = 0
        # 놓지 않고 다음 탐색
        DFS(idx + 1, cur_cnt)
            

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
bishop = [[0 for _ in range(N)] for _ in range(N)]

need_to_fill = []
for r in range(N):
    for c in range(N):
        if A[r][c] == 1:
            need_to_fill.append((r, c))

max_depth = len(need_to_fill)
DFS(0, 0)

print(max_cnt)