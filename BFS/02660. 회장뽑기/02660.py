import sys; input = sys.stdin.readline
from collections import deque

N = int(input())

friend_lst = [[] for _ in range(N+1)]
scores = [[] for _ in range(N+1)]

def read_data():
    while True:
        a, b = map(int, input().split())
        if a == -1: break
        friend_lst[a].append(b)
        friend_lst[b].append(a)

def find_min_path(start:int, end:int):
    visited = [False] * (N+1)

    # 초기화
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        v, path_len = queue.popleft()
        
        if v == end:
            return path_len
        
        for w in friend_lst[v]:
            if visited[w]: continue
            visited[w] = True
            queue.append((w, path_len + 1))

def print_result():
    for i, score in enumerate(scores):
        if not score: continue
        print(i, len(score))
        print(*score)
        return

# __main__
read_data()

# 문제 해결
for v in range(1, N+1):
    min_path_len = -1
    for w in range(1, N+1):
        if v == w: continue
        path_len_vw = find_min_path(v, w)
        if path_len_vw > min_path_len:
            min_path_len = path_len_vw
    scores[min_path_len].append(v)

print_result()