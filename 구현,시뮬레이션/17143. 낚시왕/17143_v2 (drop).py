from heapq import heappop, heappush

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
        for _ in range(self.speed):
            delta = DELTAS[self.direction]
            self.r += delta[0]
            self.c += delta[1]

            if self.r < 0:
                self.r = -self.r
                self.toggle()
            elif self.r >= row_limit:
                self.r -= 2
                self.toggle()

            if self.c < 0:
                self.c = -self.c
                self.toggle()
            elif self.c >= col_limit:
                self.c -= 2
                self.toggle()


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

    # 물고기 이동
    for i in range(ROW * COL):
        r, c = divmod(i, COL)
        if not fishery[r][c]:
            continue

        # 가장 크기가 큰 상어만 남기고 나머지는 삭제
        shark: Shark = heappop(fishery[r][c])
        fishery[r][c].clear()

        # 상어를 이동시킴
        shark.move(ROW, COL)

        # 이동한 상어를 다시 양식장에 집어 넣음
        heappush(fishery[shark.r][shark.c], shark)

print(total_size)
