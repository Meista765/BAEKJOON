N = 9
arr = [int(input()) for _ in range(N)]
arr.sort()

sum_arr = sum(arr)

for idx1 in range(N):
    for idx2 in range(idx1 + 1, N):
        if sum_arr - arr[idx1] - arr[idx2] == 100:
            for k in range(N):
                if k == idx1 or k == idx2: continue
                print(arr[k])
            exit()