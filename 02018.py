'''
- 번호 : 2018
- 제목 : 수들의 합 5
- 풀이법 :  Two-pointers
'''

N = int(input())

start_index = 1
end_index   = 1

sum = start_index
# start_index = end_index = N으로 마무리되는 경우의 수를 구현되지 않으므로 개수에 1을 추가하고 시작
cnt = 1

while end_index < N:
    if sum < N:
        end_index += 1
        sum += end_index
    elif sum == N:
        cnt += 1
        end_index += 1
        sum += end_index
    else: # sum > N
        sum -= start_index
        start_index += 1

print(cnt)