import sys
input = sys.stdin.readline
print = sys.stdout.write

def swap(pos):
    SW[pos] = [1, 0][SW[pos]]

def boy(pos):
    for idx in range(pos, N+1, pos):
        swap(idx)

def girl(pos):
    swap(pos)
    
    left = pos - 1
    right = pos + 1
    while 1 <= left <= N and 1 <= right <= N and SW[left] == SW[right]:
        swap(left)
        swap(right)
        left -= 1
        right += 1

N = int(input())
SW = [-1] + list(map(int, input().split()))

T = int(input())
for _ in range(T):
    gender, pos = map(int, input().split())
    if gender == 1:
        boy(pos)
    elif gender == 2:
        girl(pos)

for i in range(1, N+1):
    print(str(SW[i]) + ' ')