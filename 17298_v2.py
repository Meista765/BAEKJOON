N = int(input())
A = list(map(int, input().split()))
ans = [-1 for _ in range(N)]
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)

print(*ans)