import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N = int(input())

heap = []
for _ in range(N):
    start, end = map(int, input().split())
    heappush(heap, (end, start))

cnt = 0
will_end = 0
while heap:
    data = heappop(heap)
    # data[0]: 종료시간, data[1]: 시작시간
    if data[1] > will_end:
        will_end = data[0]
        cnt += 1

print(cnt)