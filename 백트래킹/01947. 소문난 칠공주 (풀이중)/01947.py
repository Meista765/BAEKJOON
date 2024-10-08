import sys
input = sys.stdin.readline

def DFS(k, pos_r, pos_c, cnt_S, cnt_Y):
    global answer
    # 임도연파가 4명 이상인 경우 탐색 중단
    if cnt_Y > 3:
        return
    
    if k == 7:
        answer += 1
        for row in visited:
            print(*row)
    else:
        # 방문 리스트 체크
        visited[pos_r][pos_c] = 1
        
        # 파벌 구성원 카운팅
        if A[pos_r][pos_c] == 'S':
            cnt_S += 1
        elif A[pos_r][pos_c] == 'Y':
            cnt_Y += 1
        
        # ↓, →, ↑, ←
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = pos_r + dr
            new_c = pos_c + dc
            if 0 <= new_r < N and 0 <= new_c < N and not visited[new_r][new_c]:
                DFS(k + 1, new_r, new_c, cnt_S, cnt_Y)
        
        # 방문 리스트 반환
        visited[pos_r][pos_c] = 0
N = 5
A = [list(input()) for _ in range(N)]

answer = 0
visited = [[0 for _ in range(N)] for _ in range(N)]

for r in range(N):
    for c in range(N):
        DFS(0, r, c, 0, 0)

print(answer)