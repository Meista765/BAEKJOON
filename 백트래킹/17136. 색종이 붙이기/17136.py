import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
# print = sys.stdout.write

from copy import deepcopy

N = 10
MAX_VALUE = 26

def make_arr_and_ones():
    """
    입력 데이터에서 1의 위치를 순회하는 함수
    """
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 1:
                ones.append((i, j))
        arr.append(row)

def check_max_squre(coord:tuple) -> int:
    """
    행렬의 정사각 크기의 최대값을 계산

    Args:
        coord (tuple): 행, 열 좌표
    """
    r, c = coord
    for size in range(1, 6, 1): # 2 ~ 5
        for nr in range(r, r+size):
            for nc in range(c, c+size):
                if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] == 0:
                    return size - 1
    return size

def make_size_arr(ones) -> list:
    size_arr = [[0] * N for _ in range(N)]
    
    for one in ones:
        r, c = one
        size_arr[r][c] = check_max_squre(one)
    
    return size_arr

def attach_paper(ones:list, rem_papers:list=[0,5,5,5,5,5]) -> None:
    global min_count
    
    if 25-sum(rem_papers) > min_count: # 사용한 종이가 최소 장수보다 많으면 가지치기
        return
    
    if len(ones) == 0:
        min_count = min(min_count, 25-sum(rem_papers))
        return
    
    r, c = ones[0]
    for size in reversed(range(1, size_arr[r][c]+1)):
        # 잔여 색종이가 남아있지 않으면 진행하지 않음
        if rem_papers[size] - 1 < 0:
            continue
        
        tmp_ones = deepcopy(ones)
        # tmp_ones.remove((r, c))
        for nr in range(r, r+size):
            for nc in range(c, c+size):
                if (nr, nc) not in tmp_ones:
                    return
                tmp_ones.remove((nr, nc))
        tmp_papers = deepcopy(rem_papers)
        tmp_papers[size] -= 1
        
        attach_paper(tmp_ones, tmp_papers)

# 입력 받기
arr = []    # 색종이를 붙여야하는 보드
ones = []   # 1이 존재하는 위치를 저장하는 리스트
size_arr = [] # 해당 위치에서 가장 넓은 사각형의 정보를 저장하는 배열

make_arr_and_ones()
size_arr = make_size_arr(ones)

# for row in size_arr:
    # print(row)

# 작업해야하는 1이 존재하지 않으면, 프로그램 종료
if len(ones) == 0:
    print(0)
    sys.exit(0)

min_count = MAX_VALUE # 각 색종이는 종류별로 5장씩 있으므로 최대 25가 나올 수 있다.

# 백트래킹
attach_paper(deepcopy(ones))

# 정답 출력
if min_count == MAX_VALUE:
    print(-1) # 정답 갱신 이력이 없는 경우,
else:
    print(min_count) # 정단 갱신이 있다면