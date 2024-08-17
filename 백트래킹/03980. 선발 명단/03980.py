import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

T = int(input())
N = 11

def DFS(player, cur_score):
    global max_score
    if player == N:
        max_score = max(max_score, cur_score)
    else:
        for pos in range(N):
            if not position[pos] and A[player][pos] != 0:
                position[pos] = 1
                DFS(player + 1, cur_score + A[player][pos])
                position[pos] = 0

for _ in range(T):
    A = [list(map(int, input().split())) for _ in range(N)]
    position = [0 for _ in range(N)]
    
    max_score = float('-inf')
    DFS(0, 0)
    print(max_score)