import sys; input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]  # 인접 리스트
visited = [True] + [False] * N  # 방문기록 (0번은 더미)
call_stack = []                 # 호출 스택

# 인접 리스트 생성
for _ in range(M):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

start = 0 # 탐색 시작 위치
count = 0 # 연결 요소의 개수
while not all(visited[1:]):
    for i in range(1, N+1):
        if not visited[i]:  # 방문하지 않고, 간선이 있는 꼭지점 선택
            start = i
            break

    # 최초 탐색 추가
    call_stack.append(start)

    while call_stack:  # 종료 조건: call_stack이 비었을 때,
        now = call_stack.pop()
        if not visited[now]:
            visited[now] = 1
            if adj[now]:
                call_stack.extend(adj[now])
    
    # while loop 1회당 count++
    count += 1

print(count)