# import sys; sys.stdin = open('input_01517.txt', 'r', encoding='UTF-8')

def swap(i:int, j:int) -> None:
    global A
    A[i], A[j] = A[j], A[i]

def quick_sort(S, E):
    global A

    if E <= S:
        return 
    elif E - S == 1:
        if A[S] > A[E]:
            swap(S, E)
    else:
        mid = (S + E) // 2
        pivot = A[mid]
        i = S
        j = E - 1
        
        # 중앙값을 배열 가장 오른편으로 몰아 놓음
        swap(mid, E)
        
        while i <= j:
            # 조건에 맞는 i를 찾을때까지 오른쪽 진출
            while i <= E and A[i] < pivot:
                i += 1
            
            # 조건에 맞는 j를 찾을때까지 오른쪽 진출
            while j >= S and A[j] > pivot:
                j -= 1
            
            # 조건에 맞되 i가 j보다 작을 때만 swap
            if i < j:
                swap(i, j)
                i += 1
                j -= 1
        
        # 빼놨던 swap 원위치 후 index 한 칸 전진
        swap(i, E)
        i += 1
        
        # 나머지에 대해 정렬
        quick_sort(S, j)
        quick_sort(i, E)

# A = [42, 32, 24, 60, 15, 5, 90, 45]
A = [4, 1, 3, 2, 5]
quick_sort(0, len(A)-1)

print(A)
