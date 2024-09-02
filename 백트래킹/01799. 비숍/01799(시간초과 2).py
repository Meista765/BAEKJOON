import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

answer = 0
def backtrack(k, cur_cnt):
    global answer
    
    if k == 2 * N:
        answer = max(answer, cur_cnt)
    else:
        for r in range(k+1):  # i: 0 ~ k
            c = k - r
            
            if r < N and c < N and not visited[0][r + c] and not visited[1][r + (N-1 - c)] and arr[r][c] == 1:
                visited[0][r + c] = 1
                visited[1][r + (N-1 - c)] = 1
                backtrack(k + 1, cur_cnt + 1)
                visited[0][r + c] = 0
                visited[1][r + (N-1 - c)] = 0
        
        backtrack(k + 1, cur_cnt)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방문 리스트 제작
visited = [[0] * (2 * N - 1) for _ in range(2)]

# 백트래킹
backtrack(0, 0)

# 결과 출력
print(answer)