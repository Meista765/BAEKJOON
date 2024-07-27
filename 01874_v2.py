# 해답에 있는 내용을 그대로 Copy
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
A = [int(input()) for _ in range(N)]
stack = list()
ans = str()

num = 1
for i in range(N):
    now = A[i]
    if now >= num:
        while now >= num:
            stack.append(num)
            num += 1
            ans += '+\n'
        
        stack.pop()
        ans += '-\n'
    
    else: # now < num
        if stack.pop() != now:
            print('NO')
            break
        else:
            ans += '-\n'
else: # When for-loop is successfully finished
    print(ans)