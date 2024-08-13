from queue import PriorityQueue

N = int(input())

pos = PriorityQueue()       # 양수를 저장 (최대힙)
negZero = PriorityQueue()   # 음수, 0 저장 (최소힙)

for _ in range(N):
    item = int(input())
    if item > 0:
        pos.put(item)
    else:
        negZero.put(item)

result = 0
while len(pos) > 1:
    a, b = pos.get(), pos.get()
    if a * b > a + b:
        result += a * b
    else:
        result += a
        pos.put(b)