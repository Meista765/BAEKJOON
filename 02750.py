# O(n^2)
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
A = list(int(input()) for _ in range(N))

for end in reversed(range(N)): # N-1 ~ 0
    for i in range(end): # 0 ~ end-1
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]

for each in A:
    print(str(each) + '\n')