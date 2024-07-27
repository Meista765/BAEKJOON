import sys
from queue import PriorityQueue

input = sys.stdin.readline
N = int(input())
data = [int(input()) for _ in range(N)]

myQueue = PriorityQueue()
for cmd in data:
    if cmd != 0:
        # 우선순위 설정: 1순위 - 절대값, 2순위 - 값의 대소
        priority = abs(cmd)
        value = cmd
        # 데이터 삽입
        myQueue.put((priority, value))
    else: # cmd == 0
        # 큐가 비어있다면, 
        if myQueue.empty() == True:
            # 0을 출력
            print(0)
        # 큐에 내용물이 있다면
        else:
            # 큐의 내용물 중 값만 출력
            print(myQueue.get()[1])