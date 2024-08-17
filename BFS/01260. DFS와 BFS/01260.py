import sys
input = sys.stdin.readline
print = sys.stdout.write

from collections import deque

V, E, S = map(int, input().split())

adj_mtrx = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

def DFS(v):
    visited[v] = 1
    print(str(v) + ' ')

    # v: 출발점, w: 도착점
    for w in range(1, V+1):
        if adj_mtrx[v][w] and not visited[w]:
            DFS(w)

def BFS(v):
    queue = deque()
    # append == push
    queue.append(v)
    visited[v] = 1

    while queue:
        # popleft == pop
        v = queue.popleft()
        print(str(v) + ' ')

        # v: 출발점, w: 도착점
        for w in range(1, V + 1):
            if adj_mtrx[v][w] and not visited[w]:
                queue.append(w)
                visited[w] = 1


# Adjacency Matrix 제작
for _ in range(E):
    v1, v2 = map(int, input().split())
    adj_mtrx[v1][v2] = 1
    adj_mtrx[v2][v1] = 1

DFS(S)
print('\n')

visited = [0 for _ in range(V+1)]
BFS(S)


