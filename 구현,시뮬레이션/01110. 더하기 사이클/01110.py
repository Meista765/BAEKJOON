'''
- 번호 : 1110
- 제목 : 더하기 사이클
'''

import sys
input = sys.stdin.readline

N = int(input())

def make_new_number(n_in: int):
    # 1. 각 자리 숫자의 합을 구한다.    
    tmp = n_in
    digit_sum = 0
    while tmp:
        digit_sum += tmp % 10
        tmp //= 10
    
    # 2. 기존의 수와 새로 구한 수의 오른쪽 자리 수를 합한 수를 반환
    return int(str(n_in)[-1] + str(digit_sum)[-1])

num = N
cnt = 0
while True:
    num = make_new_number(num)
    cnt += 1
    if num == N:
        break

print(cnt)