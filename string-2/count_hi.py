def count_hi(str):
  count_hi = 0
  for i in range(len(str)-1):
    if str[i:(i+2)] == 'hi':
      count_hi += 1
  return count_hi

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))