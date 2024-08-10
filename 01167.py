import sys
input = sys.stdin.readline

from collections import deque

V = int(input())

def find_radius():
    queue = deque()
    
    distance = [0] * (V+1)
    for i in range(1, V+1):
        if adj[i]:
            visited[i] = 1
            for data in adj[i]:
                visited[data[0]] = 1
                distance[data[0]] = data[1]
                queue.append(data)
            break
    
    while queue:
        
        
        for 
    


# 인접행렬 데이터 구조: (목적지, 가중치)
adj = [[] for _ in range(V+1)]

# 방문 리스트
visited = [0] * (V+1)

# 인접 행렬 제작
for _ in range(V):
    row = list(map(int, input().split()))
    
    v1 = row[0]
    for i in range((len(row) - 2) // 2):
        v2 = row[2 * i + 1]
        weight = row[2 * i + 2]
        
        adj[v1].append((v2, weight))

