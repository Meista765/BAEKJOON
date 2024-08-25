import sys
input = sys.stdin.readline

from collections import deque

len_r, len_c = map(int, input().split())

# 작업 좌표를 추가해주는 함수
def fill_queue():
    global queue
    
    # 작업 좌표는 0과 9가 아니며, 본인을 기준으로 8방향에 0이 있는 모래성
    for r in range(len_r):
        for c in range(len_c):
            if A[r][c] != 0 and A[r][c] != 9:
                # 8방향: ↓, ↘, →, ↗, ↑, ↖, ←, ↙
                for dr, dc in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < len_r and 0 <= nc < len_c and A[nr][nc] == 0:
                        queue.append((r, c))
                        break

A = []
for _ in range(len_r):
    cli = input().rstrip().replace('.','0')
    A.append(list(map(int, list(cli))))

queue = deque()

wave = 0
while True:
    # 작업 좌표 추가
    fill_queue()
    
    # 추후 0으로 덮어씌울 작업 리스트
    working_list = deque()
    # 한 바퀴 순회
    while queue:
        r, c = queue.popleft()
        
        # 작업 구간 주변 8방향으로 0이 몇개인지 카운트
        cnt = 0
        # 8방향: ↓, ↘, →, ↗, ↑, ↖, ←, ↙
        for dr, dc in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len_r and 0 <= nc < len_c and A[nr][nc] == 0:
                cnt += 1
        
        # 탐색 후 카운트가 탐색중인 칸의 값보다 크거나 같으면 모래성을 허묾
        if cnt >= A[r][c]:
            working_list.append((r, c))
    
    # 작업할 내용이 없으면 break
    if not working_list:
        break
    else:
        # 작업 리스트에 있는 좌표를 모두 0으로 바꿈
        while working_list:
            r, c = working_list.popleft()
            A[r][c] = 0
    
    # 반복 한 사이클 추가
        wave += 1
    
    # # 디버그용 코드
    # print(f'#{wave}')
    # for row in A:
    #     print(*row)
    # print()

print(wave)