import sys
input = sys.stdin.readline

N = int(input())
A = [tuple() for _ in range(N)]

for idx in range(N):
    A[idx] = tuple(map(int, input().split()))

A = sorted(A, key=lambda x: (x[1], x[0]))

# enum
START = 0
END = 1

cnt = 0
prev_meeting = (0, 0)
for new_meeting in A:
    if new_meeting[START] >= prev_meeting[END]:
        prev_meeting = new_meeting
        cnt += 1

print(cnt)