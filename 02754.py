word = input().rstrip()

score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D+', 'D0', 'D-']
if word not in score:
  print(f'{0.0}')
else:
  a, b = divmod(score.index(word), 3)
  print(f'{4.3 - a - 0.3 * b:.1f}')