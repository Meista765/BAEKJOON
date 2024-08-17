import sys
input = sys.stdin.readline

N = int(input())
scores = [0] * N

# 역순으로 입력 받음
for idx in range(N):
    scores[N-1 - idx] = int(input())

# 이전 score보다 1개 적은 값이 될때까지 현재 score를 감소시킴
decreased_cnt = 0
for idx in range(1, N):
    if scores[idx] >= scores[idx - 1]:
        decreased_cnt += scores[idx] - (scores[idx - 1] - 1)
        scores[idx] = scores[idx - 1] - 1

print(decreased_cnt)