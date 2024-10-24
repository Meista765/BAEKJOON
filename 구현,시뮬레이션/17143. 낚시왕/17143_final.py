import sys

input = sys.stdin.readline

R, C, remaining_sharks = map(int, input().split())

UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4

SPEED = 0
DIR = 1
SIZE = 2

board = [[None] * C for _ in range(R)]
# 입력 받기
for _ in range(remaining_sharks):
    r, c, *shark = map(int, input().split())
    if board[r - 1][c - 1]:
        if board[r - 1][c - 1][SIZE] < shark[SIZE]:
            board[r - 1][c - 1] = shark
            remaining_sharks -= 1
    else:
        board[r - 1][c - 1] = shark

man = -1  # 낚시꾼의 위치
total_size = 0  # 낚시꾼이 낚은 물고기 크기의 총합
horizontal_lst = list(range(C)) + list(range(C - 2, 0, -1))
vertical_lst = list(range(R)) + list(range(R - 2, 0, -1))
while man < C - 1 and remaining_sharks:
    man += 1

    # 낚시
    for r in range(R):
        if board[r][man]:
            total_size += board[r][man][SIZE]
            board[r][man] = None
            remaining_sharks -= 1
            break

    # 상어 이동
    new_board = [[None] * C for _ in range(R)]
    for idx in range(R * C):
        r, c = divmod(idx, C)
        if not board[r][c]:
            continue

        shark = board[r][c]  # 상어 선택
        new_r = new_c = None

        match shark[DIR]:
            case 1: # UP
                width = (R - 1) * 2
                i = (r - shark[SPEED]) % width
                if i >= R:
                    shark[DIR] = DOWN
                new_r = vertical_lst[i]

            case 2: # DOWN
                width = (R - 1) * 2
                i = (r + shark[SPEED]) % width
                if i >= R:
                    shark[DIR] = UP
                new_r = vertical_lst[i]

            case 3: # RIGHT
                width = (C - 1) * 2
                j = (c + shark[SPEED]) % width
                if j >= C:
                    shark[DIR] = LEFT
                new_c = horizontal_lst[j]

            case 4: # LEFT
                width = (C - 1) * 2
                j = (c - shark[SPEED]) % width
                if j >= C:
                    shark[DIR] = RIGHT
                new_c = horizontal_lst[j]

            case _:
                raise KeyError('잘못된 방향이 입력되었습니다.')

        if new_r is not None:
            if new_board[new_r][c]:
                if new_board[new_r][c][SIZE] < shark[SIZE]:
                    new_board[new_r][c] = shark
                    remaining_sharks -= 1
            else:
                new_board[new_r][c] = shark

        if new_c is not None:
            if new_board[r][new_c]:
                if new_board[r][new_c][SIZE] < shark[SIZE]:
                    new_board[r][new_c] = shark
                    remaining_sharks -= 1
            else:
                new_board[r][new_c] = shark

    board = new_board

print(total_size)
