import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

max_cnt = 0
def backtrack(idx:int, cur_cnt:int, visited:list):
    global max_cnt
    
    # 최대 깊이에 도달했을 때
    if idx == max_depth:
        max_cnt = max(max_cnt, cur_cnt)
    else:
        pos_r, pos_c = coord[idx]
        
        # Case 1) 해당 자리에 비숍을 배치할 수 있음
        if not visited[pos_r][pos_c]:
            # Case 1-1) 배치하지 않음 -> 다음 배치할 수 있는 위치에 배치함
            for i in range(idx + 1, max_depth):
                r, c = coord[i]
                if not visited[r][c]:
                    backtrack(i, cur_cnt, visited)
                    break
            else:
                backtrack(max_depth, cur_cnt, visited)
            
            # Case 1-2) 배치함
            # 방문 체크
            visited[pos_r][pos_c] = 1
            # ↖, ↗, ↙, ↘
            for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                new_r = pos_r + dr
                new_c = pos_c + dc
                while 0 <= new_r < N and 0 <= new_c < N:
                    visited[new_r][new_c] = 1
                    new_r += dr
                    new_c += dc
            
            for i in range(idx + 1, max_depth):
                r, c = coord[i]
                if not visited[r][c]:
                    backtrack(i, cur_cnt + 1, visited)
                    break
            else:
                backtrack(max_depth, cur_cnt + 1, visited)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 방문해야 하는 좌표 수집
coord = []
for r in range(N):
    for c in range(N):
        if A[r][c] == 1:
            coord.append((r, c))

max_depth = len(coord)

backtrack(0, 0, [[0 for _ in range(N)] for _ in range(N)])

print(max_cnt)