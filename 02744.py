def isCapital(word_in):
  if ord(word_in) >= 65 and ord(word_in) <=90:
    return True
  return False

word = input().rstrip()
ans = ''
for a in word:
  if isCapital(a):
    ans += chr(ord(a) + 32)
  else:
    ans += chr(ord(a) - 32)

print(ans)