import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def fill_chklst(pos_r:int, pos_c:int, num:int, fill:int) -> None:
    '''
    체크리스트를 원하는 수로 채우는 함수\n
    :param pos_r: 행 인덱스\n
    :param pos_c: 열 인덱스\n
    :param num: 스도쿠에 들어갈 숫자\n
    :param fill: 0(False) 또는 1(True)
    '''
    chklst_row[pos_r][num] = fill
    chklst_col[pos_c][num] = fill
    chklst_block[pos_r // 3][pos_c // 3][num] = fill

def is_fine(pos_r, pos_c, num) -> bool:
    '''
    스도쿠의 해당 위치에 원하는 숫자가 들어가도 되는지를 확인하는 함수\n
    :param pos_r: 행 인덱스\n
    :param pos_c: 열 인덱스\n
    :param num: 스도쿠에 들어갈 숫자
    '''
    return not chklst_row[pos_r][num] and not chklst_col[pos_c][num] and not chklst_block[pos_r // 3][pos_c // 3][num]

# DFS
def DFS(idx):
    # 최대 깊이 도달시 출력 후 종료
    if idx == max_depth:
        for row in A:
            print(*row)
        return
    else:
        pos_r, pos_c = need_to_fill[idx]
        for num in range(1, 10):  # num= 1 ~ 9
            # 체크리스트 3개를 모두 확인하고 삽입해도 되는 수라면, 
            if is_fine(pos_r, pos_c, num):
                # 체크리스트 기록 후 숫자 변경
                fill_chklst(pos_r, pos_c, num, 1)
                A[pos_r][pos_c] = num
                # 다음 탐색 개시
                DFS(idx + 1)
                # 복귀 시 체크리스트 및 숫자 원복
                fill_chklst(pos_r, pos_c, num, 0)
                A[pos_r][pos_c] = 0


N = 9
# 행, 열, 블럭별 체크리스트; 0번은 dummy
chklst_row = [[0] * (N+1) for _ in range(N)]
chklst_col = [[0] * (N+1) for _ in range(N)]
chklst_block = [[[0] * (N+1) for _ in range(3)] for _ in range(3)]

A = [list(map(int, input().split())) for _ in range(N)]

# 사전 준비
need_to_fill = []  # 채워야 하는 데이터의 (행, 열) 정보를 저장
for pos_r in range(N):
    for pos_c in range(N):
        if A[pos_r][pos_c] == 0:
            need_to_fill.append((pos_r, pos_c))
        else:  
            num = A[pos_r][pos_c]  # 1 ~ 9
            fill_chklst(pos_r, pos_c, num, 1)

# DFS 최대 깊이는 채워야 하는 데이터의 개수
max_depth = len(need_to_fill)

DFS(0)