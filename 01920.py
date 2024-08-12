import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
num_lst = list(map(int, input().split()))
num_lst.sort()

M = int(input())
num_to_find = list(map(int, input().split()))

def binary_search(start, end) -> int:
    global found
    global finding
    if start > end:
        return 
    elif start == end:
        if num_lst[start] == finding:
            found = 1
    else:  # start < end
        mid = (start + end) // 2
        if num_lst[mid] == finding:
            found = 1
        elif num_lst[mid] > finding:
            binary_search(start, mid-1)
        else:
            binary_search(mid+1, end)
            
for finding in num_to_find:
    found = 0
    binary_search(0, N-1)
    print(str(found) + '\n')