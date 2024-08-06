import sys
sys.setrecursionlimit(10000)  # 없으면 RecursionError 발생
input = sys.stdin.readline    # 없으면 시간초과 발생

N, M = map(int, input().split())

ADJ = [[] for _ in range(N+1)]  # 인접 리스트
VISITED = [False] * (N+1)       # 방문기록

def DFS(start):
    # 방문 기록 check
    VISITED[start] = 1
    for end in ADJ[start]:
        if VISITED[end] == 0:
            DFS(end)

# 인접 리스트 생성
for _ in range(M):
    start, end = map(int, input().split())
    ADJ[start].append(end)
    ADJ[end].append(start)

count = 0
for i in range(1, N+1):  # i: 1 ~ N
    if not VISITED[i]:
        count += 1
        DFS(i)

print(count)