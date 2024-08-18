import sys
input = sys.stdin.readline

from collections import deque

def sectioning(start_r, start_c, mode):
    '''
    :param mode: 0: 일반, 1: 적록색약
    '''
    queue = deque()
    VISITED[start_r][start_c] = 1
    queue.append((start_r, start_c))
    
    # 'R', 'G', 'B'
    color = A[start_r][start_c]
    color_pair = dict()
    if mode == 0:
        color_pair = {
            'R': ['R'],
            'G': ['G'],
            'B': ['B']
        }
    elif mode == 1:
        color_pair = {
            'R': ['R', 'G'],
            'G': ['R', 'G'],
            'B': ['B']
        }
    
    while queue:
        pos_r, pos_c = queue.popleft()
        
        # →, ↓, ←, ↑
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r = pos_r + dr
            new_c = pos_c + dc
            if 0 <= new_r < N and 0 <= new_c < N and not VISITED[new_r][new_c] and A[new_r][new_c] in color_pair[color]:
                VISITED[new_r][new_c] = 1
                queue.append((new_r, new_c))

def find_remaining():
    '''
    방문하지 않은 좌표가 있다면 해당 좌표를 반환, 만약 모두 방문했다면 -1, -1을 반환
    '''
    for r in range(N):
        for c in range(N):
            if not VISITED[r][c]:
                return r, c
    return -1, -1

def solve(mode):
    global VISITED
    cnt = 0
    VISITED = [[0 for _ in range(N)] for _ in range(N)]
    
    while True:
        start_r, start_c = find_remaining()
        
        # 더 이상 탐색할 좌표가 없다면 break
        if start_r == -1 and start_c == -1:
            break
        else:
            sectioning(start_r, start_c, mode)

        # 구획나누기를 한 번 실행할때마다 1 증가
        cnt += 1
    
    return cnt

N = int(input())
A = [list(input().rstrip()) for _ in range(N)]

VISITED = [[0 for _ in range(N)] for _ in range(N)]

print(solve(0), solve(1))