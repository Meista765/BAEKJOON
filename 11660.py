import sys
input = sys.stdin.readline

# 행렬 크기(N), 반복횟수(M)
N, M = map(int, input().split())
num_matrix = [list(map(int, input().split())) for _ in range(N)]

# (N+1) * (N+1) 부분합 행렬 구하기
sum_matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum_matrix[i][j] = num_matrix[i-1][j-1] + sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1]

ans = []
for _ in range(M):
    # 좌표 입력
    x1, y1, x2, y2 = map(int, input().split())
    
    # 결과 계산
    ans.append(sum_matrix[x2][y2] - sum_matrix[x2][y1-1] - sum_matrix[x1-1][y2] + sum_matrix[x1-1][y1-1])
    
    # 결과 출력
    sys.stdout.write('\n'.join(map(str, ans)))