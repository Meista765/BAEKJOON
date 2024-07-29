import sys
print = sys.stdout.write

A = list(map(int, list(input())))

for i in sorted(A, reverse=True):
    print(str(i))