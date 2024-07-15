import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numLst = list(map(int, input().split()))

# 부분합 array 만들기
tmp = 0
sub = [0]
for num in numLst:
    tmp = tmp + num
    sub.append(tmp)

# 결과 도출
for _ in range(M):
    s, e = map(int, input().split())
    print(sub[e] - sub[s-1])