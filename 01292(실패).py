'''
- 번호 : 1292
- 제목 : 쉽게 푸는 문제
- 핵심 : 수열의 합 (sigma N, sigma N^2)
'''

import sys
input = sys.stdin.readline

# 자연수 N의 합; 33인 이유는 32까지 갔을 때 숫자의 갯수가 1,056개로 문제 조건인 1,000개를 넘어감
sigma_n = [0 for _ in range(33)]

# 자연수 N^2의 합
sigma_n_sqr = [0 for _ in range(33)]

# 합 배열을 생성
for n in range(1, 33): # i: 1 ~ 32
    sigma_n[n] = n * (n+1) // 2
    sigma_n_sqr[n] = n * (n+1) * (2*n+1) // 6

# 인덱스 입력
start, end = map(int, input().split())

# 정답을 저장하는 변수
sum = 0

# start <= sigma(i, n)인 i를 탐색
i = 0
for idx in range(1, 33):
    if start <= sigma_n[idx]:
        i = idx
        break

# end < sigma(j, n)인 j를 탐색
j = 0
for idx in range(1, 33):
    if end < sigma_n[idx]:
        j = idx - 1
        if end == sigma_n[idx]:
            sum += j
        break

# sum 계산
sum += ((sigma_n[i] - start + 1) * i) + ((end - sigma_n[j]) * (j + 1)) + (sigma_n_sqr[j] - sigma_n_sqr[i])

# 결과 출력
print(sum)