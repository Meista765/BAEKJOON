from heapq import heappop, heappush

# 전역 변수
DIRECTION = {
    1: (-1, 0),  # UP
    2: (1, 0),  # DOWN
    3: (0, 1),  # RIGHT
    4: (0, -1),  # LEFT
}

ROW = None
COL = None
N = None


# 클래스
class Shark:
    def __init__(self, r: int, c: int, speed: int, direction: int, size: int) -> None:
        self.r = r
        self.c = c
        self.speed = speed
        self.direction = direction
        self.size = size

    # 트릭 1; 대소 비교를 반대로 만들어, heapq를 운용한다.
    def __lt__(self, other): # less than
        return self.size > other.size

    def __le__(self, other): # less than and equal to
        return self.size >= other.size

    def __gt__(self, other): # greater than
        return self.size <= other.size

    def __ge__(self, other): # greater than equal to
        return self.size < other.size

    def __eq__(self, other): # equal to
        return self.size == other.size

    def __ne__(self, other): # not equal to
        return self.size != other.size


class Fishery:
    class Fisherman:
        def __init__(self, position:int=0) -> None:
            self.position = position
            self.row, self.col = get_outer_vars()
    
    def __init__(self, row: int, col: int, sharks_count: int) -> None:
        self.row = row
        self.col = col
        self.sharks_count = sharks_count
        
        self.fishery = [[[] for _ in range(col+1)] for _ in range(row+1)]
        self.fisherman = self.Fisherman()
        for _ in range(sharks_count):
            r, c, speed, direction, size = map(int, input().split())
            shark: Shark = Shark(r, c, speed, direction, size)
            heappush(self.fishery[r][c], shark)
    
    def get_outer_vars(self):
        return self.row, self.col
    
    # 물고기를 잡는 함수
    def _catch(self):
        pass
    
    def tick(self)
        
