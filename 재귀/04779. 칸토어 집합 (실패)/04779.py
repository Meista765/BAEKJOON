import sys
input = sys.stdin.readline
print = sys.stdout.write

def make_line(k) -> str:
    if k == N:
        return '_'
    else:
        return make_line(k + 1) + ' ' * (3 ** (N-1 - k)) + make_line(k + 1)

while True:
    try:
        N = int(input())
        print(make_line(0) + '\n')
    except:
        break