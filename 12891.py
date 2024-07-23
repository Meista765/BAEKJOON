'''
- 번호 : 12891
- 제목 : DNA 비밀번호
- 기술 : 슬라이딩 윈도우
'''

import sys
input = sys.stdin.readline

# Global variables
S, P = map(int, input().split()) # 문자열 크기, 윈도우 크기
A = input() # 문자열 데이터
count = 0 # 결과를 저장하는 변수(int)

check_list = [] # int list; 비밀번호 체크 리스트
my_list = [0] * 4 # int list; 현재 상태 리스트
achieved = 0 # int; 충족 조건 개수를 저장하는 변수

# Define functions
def my_add(dna:str):
    # my_list에 새로운 값을 더하고, 조건에 따라 achieved 확인
    global achieved, my_list, check_list

    if dna == 'A':
        my_list[0] += 1
        if my_list[0] == check_list[0]:
            achieved += 1
    elif dna == 'C':
        my_list[1] += 1
        if my_list[1] == check_list[1]:
            achieved += 1
    elif dna == 'G':
        my_list[2] += 1
        if my_list[2] == check_list[2]:
            achieved += 1
    elif dna == 'T':
        my_list[3] += 1
        if my_list[3] == check_list[3]:
            achieved += 1


def my_remove(dna:str):
    # my_list에 새로운 값을 제거하고 조건에 따라 achieved update
    global achieved, my_list, check_list

    if dna == 'A':
        my_list[0] -= 1
        if my_list[0] == check_list[0] - 1:
            achieved -= 1
    elif dna == 'C':
        my_list[1] -= 1
        if my_list[1] == check_list[1] - 1:
            achieved -= 1
    elif dna == 'G':
        my_list[2] -= 1
        if my_list[2] == check_list[2] - 1:
            achieved -= 1
    elif dna == 'T':
        my_list[3] -= 1
        if my_list[3] == check_list[3] - 1:
            achieved -= 1

# main

# 1. check_list 데이터 받기
check_list = list(map(int, input().split()))

# 2. check_list를 탐색하여 값이 0인 데이터의 개수만큼 achieved 값 증가
for i in range(4):
    if check_list[i] == 0:
        achieved += 1

# 3. 최초 데이터의 유효성 판단
for i in range(P): # 0 ~ P-1
    my_add(A[i])

if achieved == 4:
    count += 1

# 4. P ~ S-1까지 탐색
for new in range(P, S):
    old = new - P
    my_remove(A[old])
    my_add(A[new])
    if achieved == 4:
        count += 1

# 5. 결과 출력
print(count)