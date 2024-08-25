import sys
input = sys.stdin.readline

from collections import deque

len_r, len_c = map(int, input().split())

A = []
for _ in range(len_r):
    cli = input().rstrip().replace('.','0')
    A.append(list(map(int, list(cli))))

queue = deque()
for r in range(len_r):
    for c in range(len_c):
        if A[r][c] != 0 and A[r][c] != 9:
            queue.append((r, c))

wave = 0
# 이전 Queue 사이즈와 변동이 없으면 반복 종료
prev_q_size = len(queue)
while queue:
    # 한 바퀴 순회
    for _ in range(len(queue)):
        pos_r, pos_c = queue.popleft()
        
        # 8방향 인근에 열려있는 개수 
        cnt = 0
        # 8방향: ↓, ↘, →, ↗, ↑, ↖, ←, ↙
        for dr, dc in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
            new_r = pos_r + dr
            new_c = pos_c + dc
            if 0 <= new_r < len_r and 0 <= new_c < len_c and A[new_r][new_c] == 0:
                cnt += 1
        
        # 본인보다 크거나 같은 수의 0이 주변에 있다면 무너뜨림
        if cnt >= A[pos_r][pos_c]:
            A[pos_r][pos_c] = 0
        # 그렇지 않으면 추후 작업을 위해 큐에 다시 보관
        else:
            queue.append((pos_r, pos_c))
    
    # 반복 한 사이클 완료
    wave += 1
    
    # 이후 반복 여부 확인
    if prev_q_size > len(queue):
        prev_q_size = len(queue)
    # prev_q_size <= len(queue) 이지만 사실상 prev_q_size == len(queue)
    else: 
        break
    
    # 디버그용 코드
    for row in A:
        print(*row)

print(wave)