import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

cnt = 0
rem = K
for i in reversed(range(N)):
    q, r = divmod(rem, coins[i])
    if q > 0:
        cnt += q
        rem = r
    if rem == 0:
        break

print(cnt)