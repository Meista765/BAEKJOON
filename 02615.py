N = 19
board = [list(map(int, input().split())) for _ in range(N)]

def garo(pos_i, pos_j, color):
    ni = pos_i
    cnt = 0
    for dj in range(6):
        nj = pos_j + dj
        if nj < N and board[ni][nj] == color:
            cnt += 1
    if cnt == 5:
        return True, color
    else:
        return False

def sero(pos_i, pos_j, color):
    nj = pos_j
    cnt = 0
    for di in range(6):
        ni = pos_i + di
        if ni < N and board[ni][nj] == color:
            cnt += 1
    if cnt == 5:
        return True
    else:
        return False

def daegak(pos_i, pos_j, color):
    cnt = 0
    for d in range(6):
        ni = pos_i + d
        nj = pos_j + d
        if ni < N and nj < N and board[ni][nj] == color:
            cnt += 1
    if cnt == 5:
        return True
    else:
        return False

def rdaegak(pos_i, pos_j, color):
    cnt = 0
    for d in range(6):
        ni = pos_i + d
        nj = pos_j - d
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == color:
            cnt += 1
    if cnt == 5:
        return True
    else:
        return False

win = False
for i in range(N):
    for j in range(N):
        color = board[i][j]
        if 0 <= j - 1 and board[i][j-1] != color:
            win |= garo(i, j, color)
        if 0 <= i - 1 and board[i-1][j] != color:
            win |= sero(i, j, color)
        if 0 <= i - 1 and 0 <= j - 1 and board[i - 1][j - 1] != color:
            win |= daegak(i, j, color)
        if 0 <= i - 1 and j + 1 < N and board[i - 1][j + 1] != color:
            win |= rdaegak(i, j, color)
        if win:
            print(color)
            print(i+1, j+1)
            break
    if win: break
else:
    print(0)