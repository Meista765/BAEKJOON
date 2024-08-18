import sys

in_str = sys.stdin.readline().rstrip()

num = ''
is_minus = False
answer = 0
tmp_sum = 0
for ch in in_str:
    if ch == '+' or ch == '-':
        tmp_sum += int(num)
        num = ''
        if ch == '-':
            if is_minus:
                answer -= tmp_sum
            else:
                answer += tmp_sum
                is_minus = True
            tmp_sum = 0
    else:
        num += ch

# 자투리 처리
tmp_sum += int(num)
if is_minus:
    answer -= tmp_sum
else:
    answer += tmp_sum

sys.stdout.write(str(answer))