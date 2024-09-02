import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def backtrack(positions, idx, count):
    global max_count
    if idx == len(positions):
        max_count = max(max_count, count)
        return

    r, c = positions[idx]
    if not visited[0][r + c] and not visited[1][r - c + N - 1]:
        visited[0][r + c] = True
        visited[1][r - c + N - 1] = True
        backtrack(positions, idx + 1, count + 1)
        visited[0][r + c] = False
        visited[1][r - c + N - 1] = False

    backtrack(positions, idx + 1, count)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방문 리스트 제작
visited = [[False] * (2 * N - 1) for _ in range(2)]

# 흑과 백 칸을 분리하여 비숍을 놓을 수 있는 위치를 미리 계산
black_positions = []
white_positions = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            if (i + j) % 2 == 0:
                black_positions.append((i, j))
            else:
                white_positions.append((i, j))

# 각 색에 대해 최대 비숍의 수를 구한 뒤 합산
max_count = 0
backtrack(black_positions, 0, 0)
black_max = max_count

max_count = 0
backtrack(white_positions, 0, 0)
white_max = max_count

# 최종 결과 출력
print(black_max + white_max)
