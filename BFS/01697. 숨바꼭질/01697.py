import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

position_limit = 100001
visited = [0] * position_limit

queue = deque()

visited[N] = 1
queue.append((N, 0))

while queue:
    position, time_past = queue.popleft()
    
    if position == K:
        print(time_past)
        break
    else:
        for new_position in [position + 1, position - 1, position * 2]:
            if -1 < new_position < position_limit and not visited[new_position]:
                visited[new_position] = 1
                queue.append((new_position, time_past + 1))