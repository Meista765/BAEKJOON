import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

found = False
def we_are_friends(n:int, recursion:int):
    global found
    visited[n] = 1
    
    if recursion == 5:
        found = True
        return
    
    for each in A[n]:
        if not visited[each]:
            we_are_friends(each, recursion + 1)

    # 깊이 방향 탐색을 마치고 빠져나오면 다른 탐색을 위해 방문 list를 리셋
    visited[n] = 0



V, E = map(int, input().split())
A = [[] for _ in range(V)]

for _ in range(E):
    v1, v2 = map(int, input().split())
    A[v1].append(v2)
    A[v2].append(v1)

visited = [0] * V
for i in range(V):
    we_are_friends(i, 1)
    if found:
        break

print(int(found))