import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

end = sum(A)
start = max(A)

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    
    rem = mid
    for i in range(N):
        if rem - A[i] < 0:
            cnt += 1
            rem = mid - A[i]
        else:
            rem -= A[i]
    
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)