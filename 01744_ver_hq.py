import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N = int(input())

pos = []  # 양수를 저장 (최대힙)
negZero = []  # 음수, 0 저장 (최소힙)

for _ in range(N):
    item = int(input())
    if item > 0:
        heappush(pos, (-item, item))
    else:
        heappush(negZero, item)

result = 0
while len(pos) > 1:
    a, b = heappop(pos), heappop(pos)
    if a[1] * b[1] > a[1] + b[1]:
        result += a[1] * b[1]
    else:
        result += a[1]
        heappush(pos, b)

while pos:
    result += heappop(pos)[1]

while len(negZero) > 1:
    a, b = heappop(negZero), heappop(negZero)
    if a * b > a + b:
        result += a * b
    else:
        result += a
        heappush(negZero, b)

result += sum(negZero)

print(result)