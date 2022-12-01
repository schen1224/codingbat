def last2(str):    
  count = 0
  for i in range(len(str)-2):
    if str[i:i+2] == str[-2:]:
      count += 1  
  return count

print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))