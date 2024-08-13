from heapq import heappop, heappush

N = int(input())
heap = []

for _ in range(N):
    heappush(heap, int(input()))

cnt = 0
while len(heap) > 1:
    a, b = heappop(heap), heappop(heap)
    cnt += a + b
    heappush(heap, a + b)

print(cnt)