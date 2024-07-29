import sys
input sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))

max_idx_diff = 0
sorted_A = sorted(A)

for i in range(N):
    if max_idx_diff < sorted_A[i][1] - i:
        max_idx_diff = sorted_A[i][1] - i

print(max_idx_diff + 1)