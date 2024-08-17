import sys
input = sys.stdin.readline

N = 19

def solve():
    # ↗, →, ↘, ↓
    delta = [(-1, 1), (0, 1), (1, 1), (1, 0)]
    
    for r in range(N):
        for c in range(N):
            if BOARD[r][c] != 0:
                color = BOARD[r][c]
                for dr, dc in delta:
                    # 탐색하려는 방향 이전에 같은 색의 돌이 있다면 이미 탐색한 경로이므로 pass
                    if 0 <= r - dr < N and 0 <= c - dc < N and BOARD[r - dr][c - dc] == color:
                        continue
                    
                    # 탐색 시작
                    cnt = 1
                    new_r = r + dr
                    new_c = c + dc
                    while 0 <= new_r < N and 0 <= new_c < N and BOARD[new_r][new_c] == color:
                        cnt += 1
                        new_r += dr
                        new_c += dc
                        
                        # 같은 돌이 6개 이상 있는 경우 탐색 중단
                        if cnt > 5: 
                            break
                    
                    # 탐색 개수가 5개로 일치하는 경우 정답 출력 후 함수 종료
                    if cnt == 5:
                        print(color)
                        print(r + 1, c + 1)
                        return
    
    # 해당하는 내용이 없으면 0 출력 후 함수 종료 
    print(0)
    return

## main ##
BOARD = [list(map(int, input().split())) for _ in range(N)]
solve()