'''
- 번호 : 02953.py
- 제목 : 나는 요리사다
- 핵심 : List Comprehension / List 메서드
'''

import sys
input = sys.stdin.readline

score = [sum(map(int, input().split())) for _ in range(5)]

# 최고 득점 및 우승자 번호 계산
winner_score = max(score)
winner_idx = score.index(winner_score) + 1

# 결과 출력
print(winner_idx, winner_score)