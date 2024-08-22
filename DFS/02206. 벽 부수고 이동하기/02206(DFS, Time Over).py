import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

min_path = float('inf')
def DFS(pos_r:int, pos_c:int, cur_path:int, wall_through:bool = False) -> None:
    """
    미로의 최단 경로를 찾는 함수

    Args:
        depth (int): 재귀 함수의 호출 깊이를 저장하는 변수
        pos_r (int): 탐색중인 x 좌표(행)
        pos_c (int): 탐색중인 y 좌표(열)
        cur_path (int): 탐색 경로 길이
        wall_through (bool, optional): 벽을 통과한 이력을 저장하는 변수 (Default = False)
    """

    # 전역 변수 import
    global min_path
    
    # 방문 이력 Check
    visited[pos_r][pos_c] = 1
    
    # 목적지 도착시, 최단 거리 경신
    if pos_r == len_r - 1 and pos_c == len_c - 1:
        min_path = min(min_path, cur_path)
    # 이외의 경우
    else:
        # ↓, →, ↑, ←
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = pos_r + dr
            new_c = pos_c + dc
            if 0 <= new_r < len_r and 0 <= new_c < len_c and not visited[new_r][new_c]:
                # 0이면 무조건 진행, wall-through에 변화 없음
                if maze[new_r][new_c] == 0:
                    DFS(new_r, new_c, cur_path + 1, wall_through)
                # 벽을 마주했을 때는
                else:  # maze[new_r][new_c] == 1:
                    # 벽을 부술 기회가 남아있다면 부수고 다음으로 진행
                    if not wall_through:
                        DFS(new_r, new_c, cur_path + 1, wall_through=True)
    
    # 방문 이력 반환
    visited[pos_r][pos_c] = 0

# 행과 열의 크기 받기
len_r, len_c = map(int, input().split())

# 입력 받기
maze = [list(map(int, list(input().rstrip()))) for _ in range(len_r)]

# 방문 리스트 초기화 (len_r X len_c)
visited = [[0 for _ in range(len_c)] for _ in range(len_r)]

# 깊이 우선 탐색
DFS(0, 0, 1)

# 최소 경로가 갱신되지 않았으면
if min_path == float("inf"):
    print(-1)
# 그 외에는
else:
    print(min_path)