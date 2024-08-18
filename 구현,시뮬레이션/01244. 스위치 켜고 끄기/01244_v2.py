import sys
input = sys.stdin.readline

N = int(input())
A = [-1] + list(map(int, input().split()))

T = int(input())

def switch(idx):
    A[idx] = [1, 0][A[idx]]

for _ in range(T):
    mode, idx = map(int, input().split())
    
    # 남학생
    if mode == 1:
        for i in range(idx, len(A), idx):
            switch(i)
            
    elif mode == 2:
        switch(idx)
        left = idx - 1
        right = idx + 1
        while 1 <= left < len(A) and 1 <= right < len(A) and A[left] == A[right]:
            switch(left)
            switch(right)
            left = left - 1
            right = right + 1

for start in range(1, len(A), 20):
    print(*A[start:start + 20])