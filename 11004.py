N, K = map(int, input().split())
A = list(map(int, input().split()))

def quick_sort(arr:list) -> list:
    if len(arr) < 2: # if list size is smaller than 1
        return arr
    else:
        pivot = arr[0]
        lst_left = []
        lst_right = []
        
        for num in arr[1:]:
            if num < pivot:
                lst_left.append(num)
            else: # num >= pivot
                lst_right.append(num)
        
        return quick_sort(lst_left) + [pivot] + quick_sort(lst_right)

print(quick_sort(A)[K-1])