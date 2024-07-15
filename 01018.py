import sys
input = sys.stdin.readline

m, n = map(int, input().split())
given = list()
for i in range(m):
  given.extend(input().split())

pattern1 = list()
pattern2 = list()

for i in range(8):
  if i % 2 == 1:
    pattern1.append('WB' * 4)
    pattern2.append('BW' * 4)
  else:
    pattern1.append('BW' * 4)
    pattern2.append('WB' * 4)

cnt_lst = list()

for i in range(m - 7):
  for j in range(n - 7):
    counter1 = 0
    counter2 = 0
    for r in range(i, i + 8):
      for c in range(j, j + 8):
        if given[r][c] != pattern1[r - i][c - j]:
          counter1 += 1
        if given[r][c] != pattern2[r - i][c - j]:
          counter2 += 1
    cnt_lst.append(min(counter1, counter2))

print(min(cnt_lst))