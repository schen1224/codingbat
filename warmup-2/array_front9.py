def array_front9(nums):
  for num in nums[:4]:
    if num == 9:
      return True
  return False

print(array_front9([1, 2, 9, 3, 4]) )
print(array_front9([1, 2, 3, 4, 9]) )
print(array_front9([1, 2, 3, 4, 5]))

