import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.read().splitlines()))
tmp_arr = [0] * N

def merge_sort(start, end):
    if start >= end:
        return
    
    mid = int((start + end) / 2)
    
    merge_sort(start, mid)
    merge_sort(mid+1, end)
    
    for i in range(start, end+1):
        tmp_arr[i] = A[i]
    
    tmp_idx = start
    idx_1 = start
    idx_2 = mid+1
    
    while idx_1 <= mid and idx_2 <= end:
        if tmp_arr[idx_1] < tmp_arr[idx_2]:
            A[tmp_idx] = tmp_arr[idx_1]
            idx_1 += 1
        else:
            A[tmp_idx] = tmp_arr[idx_2]
            idx_2 += 1
        tmp_idx += 1
    
    while idx_1 <= mid:
        A[tmp_idx] = tmp_arr[idx_1]
        idx_1 += 1
        tmp_idx += 1
        
    while idx_2 <= end:
        A[tmp_idx] = tmp_arr[idx_2]
        idx_2 += 1
        tmp_idx += 1

merge_sort(0, N-1)
for num in A:
    sys.stdout.write(str(num) + '\n')