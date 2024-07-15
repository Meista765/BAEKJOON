import sys
input = sys.stdin.readline

row, col = map(int, input().split())

# 행렬 정의
matrix_a, matrix_b = list(), list()

for i in range(row):
  matrix_a.append(list(map(int, input().split())))

for i in range(row):
  matrix_b.append(list(map(int, input().split())))

# 행렬 합
matrix_sum = list()
for r in range(row):
  tmp_r = list()
  for c in range(col):
    tmp_r.append(matrix_a[r][c] + matrix_b[r][c])
  matrix_sum.append(tmp_r)

for r in matrix_sum:
  print(*r)