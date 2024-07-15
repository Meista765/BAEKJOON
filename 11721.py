'''
- 번호 : 11721
- 제목 : 열 개씩 끊어 출력하기
- 핵심 : 문자열 슬라이싱의 특징
'''

import sys
input = sys.stdin.readline

inStr = input().rstrip()

while inStr:
    print(inStr[:10])
    inStr = inStr[10:]