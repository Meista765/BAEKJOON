import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numLst = list(map(int, input().split()))

# 부분합 계산
tmp = 0
sumLst = [0]
for num in numLst:
    tmp = tmp + num
    sumLst.append(tmp)

# 1 ~ N까지 바뀌는 윈도우를 가지고 탐색
cnt = 0
for w in range(1, N+1):
    # 탐색 영역은 w ~ N까지 (단, 1 <= w <= N)
    for i in range(w, N+1):
        if (sumLst[i] - sumLst[i-w]) % M == 0: 
            cnt += 1

print(cnt)