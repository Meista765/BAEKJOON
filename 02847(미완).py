'''
- 번호 : 02847
- 제목 : 게임을 만든 동준이
'''

import sys
input = sys.stdin.readline

N = int(input())
levels = [int(input()) for _ in range(N)]

# 마지막 레벨이 가장 높은 점수가 되어야 하므로 배열을 역순으로 한다.
levels.reverse()

# 정답 초기화
decrease = 0

# 최초 기준은 마지막 레벨의 점수 
criteria = levels[0]
for score in levels:
    decrease += score - criteria
    # 다음 기준은 적어도 이전 레벨보다 1점은 낮아야 한다.
    criteria -= 1

# 정답 출력
print(decrease)