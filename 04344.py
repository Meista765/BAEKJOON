'''
- 번호 : 04344.py
- 제목 : 평균은 넘겠지
'''

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 케이스 한 줄 받기
    lst = list(map(int, input().split()))
    
    # N과 lst 분리
    N = lst[0]
    lst = lst[1:]
    
    # 평균 구하기
    avg = sum(lst) / N
    
    # lst 내부에서 평균을 넘는 학생들의 수
    cnt = 0
    for num in lst:
        if num > avg: cnt += 1
    
    # 결과 출력
    print(f'{cnt/N*100:.3f}%')