import sys
input = sys.stdin.readline

max_sum = float('-inf')
def backtrack(idx, cur_cnt, cur_sum):
    global limit, max_sum
    
    if cur_cnt > 3:
        return
    
    if cur_sum > limit:
        return
    
    if idx == N:
        if cur_cnt == 3 and cur_sum <= limit:
            max_sum = max(max_sum, cur_sum)
    else:
        visited[idx] = 1
        backtrack(idx + 1, cur_cnt + 1, cur_sum + card_lst[idx])
        
        visited[idx] = 0
        backtrack(idx + 1, cur_cnt, cur_sum)

N, limit = map(int, input().split())
card_lst = list(map(int, input().split()))

visited = [0] * N

backtrack(0, 0, 0)
print(max_sum)
