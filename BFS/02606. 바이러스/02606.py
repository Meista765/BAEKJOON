import sys
input = sys.stdin.readline

from collections import deque

V = int(input())
E = int(input())

# 인접 리스트, 방문 리스트 (0번은 더미)
adj_lst = [[] for _ in range(V+1)]
visited = [0] * (V+1)

for _ in range(E):
    v1, v2 = map(int, input().split())
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1)

# 초기 설정
queue = deque()

visited[1] = 1
queue.append(1)

while queue:
    v1 = queue.popleft()
    
    for v2 in adj_lst[v1]:
        if not visited[v2]:
            visited[v2] = 1
            queue.append(v2)

print(sum(visited) - 1)