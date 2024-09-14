# Write a recursive function to find the maximum number in a list.
def max(arr):
  if len(arr) < 2:
    if len(arr) == 2:
      return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(max([1, 2, 3, 4])) # => 4