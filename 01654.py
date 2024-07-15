import sys
input = sys.stdin.readline

k, n = map(int, input().split())
ans = -1 # undefined

cables = list()
for i in range(k):
  cables.append(int(input()))

def bin_search(lower, upper):
  if upper < lower:
    return
  global n
  global ans
  middle_length = (lower + upper) // 2
  cnt = 0
  for cable in cables:
    cnt += cable // middle_length
  if cnt >= n:
    ans = middle_length
    bin_search(middle_length + 1, upper)
  else:
    bin_search(lower, middle_length - 1)

bin_search(1, max(cables))
print(ans)