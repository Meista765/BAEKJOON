import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
A = [int(input()) for _ in range(N)]
myStack = list()
ans = str()

num = 1
for i in range(N):
    # 넣어햐 하는 수가 뽑고자 하는 수보다 작거나 같다면
    if num <= A[i]:
        while num <= A[i]:
            # 삽입 후 정답에 + 마크 추가
            myStack.append(num)
            ans += '+'
            # num++
            num += 1
        
        # num == A[i]인 결과물을 pop
        myStack.pop()
        ans += '-'
    else: # num > A[i]
        found = False
        # stack이 비어있지 않다면,
        while myStack:
            # stack에서 데이터를 하나 인출하여 임시 저장
            tmp = myStack.pop() 
            ans += '-'
            # 만약 인출한 데이터가 찾는 값이라면 break
            if tmp == A[i]:
                # flag 변수를 True로 바꾸고
                found = True
                break
        
        # while-loop를 빠져 나왔을 때, 원하는 값을 찾지 못했다면
        if not found:
            # NO를 출력하고 for-loop를 빠져 나갔다면
            print('NO')
            break
# for문을 무사히 통과했다면, (도중에 break를 만나지 않고)
else:
    # 저장된 답안을 출력하자
    for ch in ans:
        print(ch + '\n')
