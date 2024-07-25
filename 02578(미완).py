'''
- 번호 : 2578
- 제목 : 빙고
'''

import sys
input = sys.stdin.readline

# 빙고 숫자 배열
BINGO = [list(map(int, input().split())) for _ in range(5)]

# 숫자가 불렸는지 확인하는 배열
CHECK = [[0 for _ in range(5)] for _ in range(5)]

# 빙고 개수
CNT = 0

def find_index(target:int) -> tuple:
    global BINGO
    for i in range(5):
        for j in range(5):
            if BINGO[i][j] == target:
                return (i, j)

def check_bingo(index:tuple):
    global CHECK, CNT
    i, j = index
    
    # 해당 위치에 check
    CHECK[i][j] = 1
    
    # i, j에 따라 수직, 수평, 대각선으로 빙고를 확인하는 메소드 구현

# 사회자가 숫자를 부르는 순서를 저장하는 배열
call = []
for _ in range(5):
    call.extend(list(map(int, input().split())))


for i in range(25):
    num = call[i]
    idx = find_index(num)
    check_bingo(idx)
    
    if CNT >= 3:
        print(num)
        break