import sys; input = sys.stdin.readline

class Frame:
    def __init__(self, capacity) -> None:
        # 데이터구조: [학생번호, 추천 횟수, 추천 시점]
        self.data = [[0, 0, 0] for _ in range(capacity)]
        # Frame 용량
        self.capacity = capacity
        # Frame 현재용량
        self.current = 0
    
    def isFull(self):
        return self.capacity == self.current
    
    def index(self, student):
        for idx, data in enumerate(self.data):
            if data[0] == student:
                return idx
        return -1
    
    def oldest(self):
        if not self.isFull():
            return -1
        old_idx = -1
        timing = float('inf')
        for data in self.data:
            
    
    def push(self, student, when):
        idx = self.index(student)
        # 추천된 적이 없다면
        if idx == -1:
            # Frame이 가득 찼다면
            if self.isFull():
                pass
            # 여유가 있다면 삽입 후 개수 증가
            else:
                self.data[self.current] = [student, 1, when]
                self.current += 1
        # 추천된 적이 있다면, 추천 횟수 추가 및 추천 시점 변경
        else:
            self.data[idx][1] += 1
            self.data[idx][2] += when


N = int(input())

# 반복 횟수
T = int(input())


FRAME = [[0, 0, 0] for _ in range(N)]


# 입력 처리
input_lst = list(map(int, input().split()))
for sequence, nominee in enumerate(input_lst):