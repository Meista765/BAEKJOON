import sys
input = sys.stdin.readline

bingo_count = 0
bingo_board = [[0 for _ in range(5)] for _ in range(5)]
def check_bingo(pos_r, pos_c):
    # x, y 좌표가 같은 경우 X 체크 추가
    # x == y: \ 체크
    # x + y == 4: / 체크
    # 공통: 가로 세로 체크
    # 호출된 번호 체크
    global bingo_count
    bingo_board[pos_r][pos_c] = 1
    
    # 해당 열 체크
    is_bingo = True
    for r in range(5):
        is_bingo &= bingo_board[r][pos_c]
    if is_bingo:
        bingo_count += 1
    
    # 해당 행 체크
    is_bingo = True
    for c in range(5):
        is_bingo &= bingo_board[pos_r][c]
    if is_bingo:
        bingo_count += 1
    
    # \ 체크
    if pos_r == pos_c:
        is_bingo = True
        for idx in range(5):
            is_bingo &= bingo_board[idx][idx]
        if is_bingo:
            bingo_count += 1
    
    # / 체크
    if pos_r + pos_c == 4:
        is_bingo = True
        for idx in range(5):
            is_bingo &= bingo_board[idx][4 - idx]
        if is_bingo:
            bingo_count += 1

coordinations = dict()

## main ##
for r in range(5):
    numbers = list(map(int, input().split()))
    for c in range(5):
        coordinations[numbers[c]] = (r, c)

call_lst = list()
for _ in range(5):
    call_lst.extend(list(map(int, input().split())))

call_count = 0
for call in call_lst:
    call_count += 1
    check_bingo(*coordinations[call])
    if bingo_count >= 3:
        print(call_count)
        break