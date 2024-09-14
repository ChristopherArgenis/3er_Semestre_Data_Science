# Write out the code for the earlier sum function.
def sum(arr):
  total = 0
  for x in arr:
    total += x
  return total

print(sum([1, 2, 3, 4])) # => 10