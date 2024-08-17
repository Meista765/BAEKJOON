A = [0] * 1001

def make_array():
    idx = 1
    number = 1
    while True:
        for _ in range(number):
            A[idx] = number
            idx += 1
            if idx == 1001:
                return
        number += 1

# main #
make_array()
start, end = map(int, input().split())

answer = 0
for idx in range(start, end + 1):
    answer += A[idx]

print(answer)