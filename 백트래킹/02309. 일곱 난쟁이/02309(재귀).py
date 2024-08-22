def DFS(idx, cnt, cur_sum):
    # Prunning
    # 현재 합이 100을 넘으면 추가 탐색 중단
    if cur_sum > 100:
        return
    
    # 8개 이상의 원소를 포함하는 경우 탐색 중단
    if cnt > 7:
        return
    
    # 결과 출력 조건
    if idx == N:
        if cnt == 7 and cur_sum == 100:
            for i in range(N):
                if visited[i]:
                    print(A[i])
            exit()
    else: # cnt < 7
        # 현 위치의 값을 포함하고 다음 진행
        visited[idx] = 1
        DFS(idx + 1, cnt + 1, cur_sum + A[idx])
        # 현 위치의 값을 포함하지 않고 다음 진행
        visited[idx] = 0
        DFS(idx + 1, cnt, cur_sum)


N = 9
A = [int(input()) for _ in range(N)]
A.sort()
visited = [0] * N

DFS(0, 0, 0)