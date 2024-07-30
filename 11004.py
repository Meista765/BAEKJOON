N, K = map(int, input().split())
A = list(map(int, input().split()))

def quick_sort(start:int, end:int, k_th:int) -> None:
    pass

def find_pivot(start:int, end:int) -> int:
    # 데이터가 2개인 경우는 바로 비교하여 정렬
    if end - start == 1:
        if A[start] > A[end]:
            A[start], A[end] = A[end], A[start]
            return start
        else:
            return end
    
    # 중앙값
    mid = (start + end) // 2
    # 중앙값을 시작 위치와 swap
    A[start], A[mid] = A[mid], A[start]
    # pivot(피벗)을 시작 위치 값 A