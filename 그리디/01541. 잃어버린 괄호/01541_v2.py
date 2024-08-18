import sys

in_str = sys.stdin.readline().rstrip()

A = in_str.split('-')
N = len(A)

sub_sum = [0] * N

answer = 0
for i in range(N):
    sub_sum[i] = sum(map(int, A[i].split('+')))
    if i == 0:
        answer += sub_sum[i]
    else:
        answer -= sub_sum[i]

sys.stdout.write(str(answer))