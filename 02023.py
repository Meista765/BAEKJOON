import sys

input = sys.stdin.readline
print = sys.stdout.write

prime_number = {2, 3, 5, 7}
# 소수인지 판별하는 함수
def is_prime_number(tgt:int) -> bool:
    # memorization 활용
    if tgt in prime_number:
        return True
    
    end = int(tgt ** (1/2))
    for i in range(2, end+1):
        if tgt % i == 0:
            return False
    
    prime_number.add(tgt)
    return True

def solve(tgt_digit:int, curr_digit:int, chk_num:int):
    '''
    :tgt_digit: 목표로 하는 자리수
    :curr_digit: 현재 검토중인 자리수, 재귀의 깊이를 나타냄
    :chk_num: 현재 검토중인 수
    '''
    # 현재 검토중인 수가 소수가 아니라면 pruning
    if not is_prime_number(chk_num):
        return
    else:  # 소수라면
        # 목표 자리수보다 깊이 들어왔다면 return
        if curr_digit > tgt_digit:
            return
        # 목표 자리수와 동일하다면 
        elif curr_digit == tgt_digit:
            print(str(chk_num) + '\n')
        else: # 목표 자리수보다 작다면
            for i in range(1, 10, 2): # 1, 3, 5, 7, 9
                solve(tgt_digit, curr_digit+1, chk_num * 10 + i)

N = int(input())

for i in [2, 3, 5, 7]:
    solve(N, 1, i)