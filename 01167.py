import sys
input = sys.stdin.readline

from collections import deque

V = int(input())

def BFS(start):
    # 방문 리스트 초기화
    visited = [0] * (V+1)
    
    # 최대 거리 저장
    distance = [0] * (V+1)
    
    # 반환값: 최대거리와 그 인덱스
    max_dist = -1
    max_idx = -1
    
    queue = deque()
    
    # 최초값 push
    visited[start] = 1
    queue.append(start)    
    
    # 큐가 빌 때까지 위 작업을 반복
    while queue:
        v1 = queue.pop()
        
        # v2: 목적지 정점, w: 가중치
        for data in adj[v1]:
            v2, w = data
            if not visited[v2]:
                visited[v2] = 1
                distance[v2] = distance[v1] + w
                if distance[v2] > max_dist:
                    max_idx = v2
                    max_dist = distance[v2]
                queue.append(v2)
    
    # test용 코드
    # print(distance[1:])
    # print('max_idx:', max_idx, ', max_dist:', max_dist)
    return (max_idx, max_dist)

# 인접행렬 데이터 구조: (목적지, 가중치)
adj = [[] for _ in range(V+1)]


# 인접 행렬 제작
for _ in range(V):
    row = list(map(int, input().split()))
    
    v1 = row[0]
    for i in range((len(row) - 2) // 2):
        v2 = row[2 * i + 1]
        weight = row[2 * i + 2]
        
        adj[v1].append((v2, weight))


# 임의의 시작 위치 선정
tmp_start = int()
for i in range(1, V+1):
    if adj[i]:
        tmp_start = i
        break

# 1회 실행하여 실제 시작 위치를 구함(임의의 정점에서 거리가 가장 먼 정점)
real_start, dummy = BFS(tmp_start)
# 실제 시작 위치에서 가장 먼 정점을 계산
dummy, answer = BFS(real_start)

print(answer)