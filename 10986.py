import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

# M으로 나누었을 때, 나머지가 남는 부분합 요소들을 저장하는 배열
remainders = [0 for _ in range(M)] 

# 부분 모듈로 계산
partial_sum = 0
for num in numbers:
    partial_sum += num
    remainder = partial_sum % M
    
    remainders[remainder] += 1

# 나머지가 0인 경우, N번째까지 요소의 부분합이 M이라는 의미이므로
ans = remainders[0]

# 나머지가 남는 부분합 중에서 2개를 택해서 S[s+1] ~ S[e]까지의 부분합 중 나머지가 없는 경우를 구하면
for cnt in remainders:
    if cnt > 1:
        ans += cnt * (cnt-1) // 2 # Combination(cnt, 2)

print(ans)