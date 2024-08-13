import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
K = int(input())

start, end = 1, K
ans = -1
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, mid // i)

    if cnt < K:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(str(ans))