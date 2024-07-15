'''
- 번호 : 2846
- 제목 : 오르막길
'''

import sys
input = sys.stdin.readline

# 조건 입력
N = int(input())
lst = list(map(int, input().split()))


ans = 0
# 배열이 하나인 경우 오르막이 성립할 수 없음
if len(lst) == 1: print(0)
else:
    start = end = lst[0]
    # 이전 STEP보다 현재 STEP이 커졌다면 END를 갱신한다
    for i in range(1, N):
        now = lst[i]
        if now > end:
            end = now
        # 이전 STEP과 차이가 없거나 오히려 줄어들었다면,
        else:
            # 정답을 갱신하고, 
            ans = max(ans, (end-start))
            # INDEX를 초기화한다.
            start = end = now
    # 오르막이 계속되서 미처 갱신되지 못한 정답을 갱신한다
    ans = max(ans, (end-start))

# 정답 출력
print(ans)