from heapq import heappop, heappush
from collections import deque

# 전역 변수
UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4

DELTAS = {
    1: (-1, 0),  # UP
    2: (1, 0),  # DOWN
    3: (0, 1),  # RIGHT
    4: (0, -1),  # LEFT
}

# 클래스
class Shark:
    def __init__(self, r: int, c: int, speed: int, direction: int, size: int) -> None:
        self.r = r
        self.c = c
        self.speed = speed
        self.direction = direction
        self.size = size

    def __repr__(self) -> str:
        arrow = ''
        if self.direction == 1:
            arrow = '↑'
        elif self.direction == 2:
            arrow = '↓'
        elif self.direction == 3:
            arrow = '→'
        else:
            arrow = '←'
            
        return f'[{self.speed}/{arrow}/{self.size}]'
    
    # 트릭 1; 대소 비교를 반대로 만들어, heapq를 운용한다.
    def __lt__(self, other):  # less than
        return self.size > other.size

    def toggle(self):
        if self.direction == UP:
            self.direction = DOWN
        elif self.direction == DOWN:
            self.direction = UP
        elif self.direction == RIGHT:
            self.direction = LEFT
        elif self.direction == LEFT:
            self.direction = RIGHT

    def move(self, row_limit: int, col_limit: int):
        vertically_move = (self.direction == UP or self.direction == DOWN)
        horizontally_move = (self.direction == RIGHT or self.direction == LEFT)
        
        limit = start = None
        
        if vertically_move: # 열 방향 이동
            limit = row_limit - 1
            start = self.r
        elif horizontally_move: # 행 방향 이동
            limit = col_limit - 1
            start = self.c
        
        # 왕복 패턴의 길이: 2 * limit
        cycle_length = 2 * limit
        
        # 이동한 위치가 왕복 사이클 내에서 어디에 있는지 계산
        remaining_moves = self.speed % cycle_length
        
        # 주어진 시작 위치에서 이동한 후 위치 계산
        position = start + remaining_moves
        
        # 이동이 경계를 넘는다면 반대 방향으로 돌아와야 한다
        if position > limit:
            position = 2 * limit - position
            self.toggle()
        
        if vertically_move:
            self.r = position
        elif horizontally_move:
            self.c = position


ROW, COL, N = map(int, input().split())

# 상어 담기
fishery = [[[] for _ in range(COL)] for _ in range(ROW)]
for _ in range(N):
    r, c, speed, direction, size = map(int, input().split())
    heappush(fishery[r - 1][c - 1], Shark(r - 1, c - 1, speed, direction, size))

# 초기화
fisherman = -1
total_size = 0

while fisherman < COL - 1:
        fisherman += 1

    # 고기 잡기
    for r in range(ROW):
        if fishery[r][fisherman]:
            shark: Shark = heappop(fishery[r][fisherman])
            fishery[r][fisherman].clear()
            total_size += shark.size
            break

    # 물고기를 모두 큐에 옮겨 담음
    queue = deque()
    for i in range(ROW * COL):
        
        r, c = divmod(i, COL)
        if not fishery[r][c]:
            continue

        # 가장 크기가 큰 상어만 남기고 나머지는 삭제
        shark: Shark = heappop(fishery[r][c])
        fishery[r][c].clear()

        # 작업해야 할 상어를 큐에 담음
        queue.append(shark)
    
    # 물고기의 이동을 반영함
    while queue:
        shark = queue.popleft()
        
        # 상어를 이동시킴
        shark.move(ROW, COL)

        # 이동한 상어를 다시 양식장에 집어 넣음
        heappush(fishery[shark.r][shark.c], shark)

print(total_size)
