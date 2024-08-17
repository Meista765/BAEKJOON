import sys
input = sys.stdin.readline

# enum
HEIGHT = 0  # 높이
WIDTH = 1  # 폭

# 높이, 폭 순서로 정렬
lengths = list(map(int, input().split()))
lengths[0], lengths[1] = lengths[1], lengths[0]

# 절단 위치 저장
cutting_points = [list(), list()]
T = int(input())
for _ in range(T):
    idx, cutting = map(int, input().split())
    cutting_points[idx].append(cutting)

# 절단 위치 정렬 후 절단
cut_length = [list(), list()]
for idx in range(2):
    cutting_points[idx].sort()
    
    prev_cut = 0
    for cut in cutting_points[idx]:
        cut_length[idx].append(cut - prev_cut)
        prev_cut = cut
    cut_length[idx].append(lengths[idx] - prev_cut)

# 최대 넓이 계산
max_area = float('-inf')
for h in cut_length[HEIGHT]:
    for w in cut_length[WIDTH]:
        if w * h > max_area:
            max_area = w * h

# 출력
print(max_area)