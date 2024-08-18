def find_rc():
    global ROW, COL
    for i in range(W):
        for j in range(H):
            if word_A[i] == word_B[j]:
                ROW = j
                COL = i
                return
            
word_A, word_B = input().split()

W = len(word_A)
H = len(word_B)

ROW = COL = -1
find_rc()

A = [['.'] * W for _ in range(H)]

for c in range(W):
    A[ROW][c] = word_A[c]

for r in range(H):
    A[r][COL] = word_B[r]

for row in A:
    print(*row, sep='')