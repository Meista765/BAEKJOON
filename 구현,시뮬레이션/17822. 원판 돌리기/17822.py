import sys

input = sys.stdin.readline

# ----- Global variables -----
# 원판 개수(N), 원판 위에 적힌 수의 개수(M), 명령어 개수(T)
N, M, T = map(int, input().split())

# ----- enum class -----
CW = 0  # 시계방향(Clock wise)
CCW = 1  # 반시계방향(Counter-clock wise)

class Plate:
    def __init__(self) -> None:
        # 2차원 배열의 0번 행은 더미
        self.numbers = [[0] * N] + [list(map(int, input().split())) for _ in range(N)]

    def __str__(self) -> str:
        rows = [" " + str(row) for row in self.numbers]
        rows.pop(0)
        return "[\n" + ",\n".join(rows) + "\n]"

    def rotate(self, multiple: int, direction: int, rot_times: int) -> None:
        """원판을 회전 시킴

        Args:
            multiple (int): 입력된 수의 배수에 해당하는 원판을 회전
            direction (int): 회전 방향
            rot_times (int): 회전 횟수
        """
        if multiple < 1:
            raise IndexError("원판의 인덱스는 1 이상이어야 합니다.")
        elif multiple > N:
            raise IndexError("원판의 인덱스가 배열을 초과합니다.")

        # 회전 횟수는 모듈러 연산을 통해 제자리로 돌아오는 경우를 없애준다.
        rot_times %= N

        if direction == CW:
            for row in range(multiple, N + 1, multiple):
                new_lst = [None] * M
                ni = 0
                for i in range(M - rot_times, M):
                    new_lst[ni] = self.numbers[row][i]
                    ni += 1
                for i in range(M - rot_times):
                    new_lst[ni] = self.numbers[row][i]
                    ni += 1
                self.numbers[row] = new_lst.copy()
        elif direction == CCW:
            for row in range(multiple, N + 1, multiple):
                new_lst = [None] * M
                ni = 0
                for i in range(rot_times, M):
                    new_lst[ni] = self.numbers[row][i]
                    ni += 1
                for i in range(rot_times):
                    new_lst[ni] = self.numbers[row][i]
                    ni += 1
                self.numbers[row] = new_lst.copy()
        else:
            raise ValueError("회전 방향은 0 또는 1이어야 합니다.")


# __main__
plate = Plate()

plate.rotate(2, 0, 1)
print(plate)
plate.rotate(3, 1, 3)
print(plate)
