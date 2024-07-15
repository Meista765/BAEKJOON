n = int(input())
numbers = list()

for i in range(n):
  numbers.append(int(input()))

def mean(data, n_data):
  return sum(data) // n_data

def median(data, n_data):
  data.sort()
  return data[n_data // 2]

def mode(data):
  data.sort()
  num = list()
  cnt = list()
  
  for datum in data:
    if datum not in num:
      num.append(datum)
      cnt.append(1)
    else:
      cnt[num.index(datum)] += 1

def inter(data):
  return max(data) - min(data)

print(mean(numbers, n))
print(median(numbers, n))
# print(mode(numbers))
print(inter(numbers))