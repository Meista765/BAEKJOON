import sys
input = sys.stdin.readline

tmp = 0
score = []
diff = []

for _ in range(10):
    tmp = tmp + int(input())
    score.append(tmp)
    diff.append(abs(tmp - 100))

score.reverse()
diff.reverse()

print(score[diff.index(min(diff))])