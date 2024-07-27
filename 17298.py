# 수열의 크기
N = int(input())

# 수열
A = list(map(int, input().split()))

# 스택
stack = list()

# 정답 배열 (default = -1)
result = [-1 for _ in range(N)]

for i in range(N):
    # stack이 비어있으면, index를 push 후 처음으로
    if not stack:
        stack.append(i)
        continue
    
    top = A[i]
    
    # stack에 기저장된 index에 대해 작업 수행
    for j in reversed(range(len(stack))):
        # 현재 확인 중인 수보다 작은 값이라면
        if A[stack[j]] < top:
            # 정답을 현재 값으로 갱신하고,
            result[stack[j]] = top
            # index 제거
            stack.pop()
        else: # 현재 확인 중인 수보다 큰 값에 봉착하면
            # loop stop
            break
    
    # 현재 보는 수의 index를 push하고 마무리
    stack.append(i)

# 정답 출력
print(*result)