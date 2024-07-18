'''
- 번호 : 12891
- 제목 : DNA 비밀번호
- 기술 : 슬라이딩 윈도우
'''

import sys
input = sys.stdin.readline

S, P = map(int, input().split())
DNA = input().rstrip()
cond = list(map(int, input().split()))

# 정답 초기화
cnt = 0

# 부분 문자열이 보유한 A,C,G,T 초기화
now = {'A': DNA[0:P].count('A'),
       'C': DNA[0:P].count('C'), 
       'G': DNA[0:P].count('G'), 
       'T': DNA[0:P].count('T')}

for i in range(0, S-P+1):
    # 부분 문자열 추출
    partial = DNA[i : i+P]
    
    # 부분 문자열 조건 확인
    is_ok = True
    for a, b in zip(now.keys(), cond):
        is_ok *= (a < b)
    
    # 조건 확인 성공시
    if is_ok:
        cnt += 1
    
    # ACGT 갱신
    now[partial[i]] -= 1
    if i+P


print(cnt)