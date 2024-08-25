import sys
input = sys.stdin.readline

from collections import deque

len_r, len_c = map(int, input().split())

# 작업 좌표를 추가해주는 함수
def fill_queue():
    global queue
    
    # 작업 좌표는 0을 기준으로 8방향에 9가 아닌 모래성
    visited = [[0 for _ in range(len_c)] for _ in range(len_r)]
    for r in range(len_r):
        for c in range(len_c):
            if A[r][c] == 0:
                # 8방향: ↓, ↘, →, ↗, ↑, ↖, ←, ↙
                for dr, dc in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
                    nr = r + dr
                    nc = c + dc
                if 0 <= nr < len_r and 0 <= nc < len_c and A[nr][nc] != 0 and A[nr][nc] != 9 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

A = []
for _ in range(len_r):
    cli = input().rstrip().replace('.','0')
    A.append(list(map(int, list(cli))))

queue = deque()

wave = 0
# 이전 Queue 사이즈와 변동이 없으면 반복 종료
prev_q_size = float('inf')
while True:
    # 작업 좌표 추가
    fill_queue()
    
    # 한 바퀴 순회
    while queue:
        r, c = queue.popleft()
        
        # 작업 구간 주변 8방향으로 0이 몇개인지 카운트
        cnt = 0
        # 8방향: ↓, ↘, →, ↗, ↑, ↖, ←, ↙
        for dr, dc in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
            nr = r + dr
            nc = c + dc
        if 0 <= nr < len_r and 0 <= nc < len_c and A[nr][nc] != 0 and A[nr][nc] != 9:
            queue.append((nr, nc))
    
    # 반복 한 사이클 완료
    wave += 1
    
    # 이후 반복 여부 확인
    if prev_q_size > len(queue):
        prev_q_size = len(queue)
    # prev_q_size <= len(queue) 이지만 사실상 prev_q_size == len(queue)
    else: 
        break
    
    # # 디버그용 코드
    # for row in A:
    #     print(*row)

print(wave)