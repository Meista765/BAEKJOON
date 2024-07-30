N = int(input())
A = list(map(int, input().split()))

# 삽입정렬 구현
for i in range(1, N): # i: 1 ~ N-1
    hold = A[i]
    for j in reversed(range(i)): # j: i-1 ~ 0
        if A[j] > hold:
            A[j+1] = A[j] # j+1: i ~ 1
        else: # A[j] <= hold
            A[j+1] = hold
            break
    else:
        A[0] = hold

# 부분합 계산
S = [0] * N
tmp_sum = 0
for i in range(N):
    tmp_sum += A[i]
    S[i] = tmp_sum

# 부분합의 합 계산
print(sum(S))
