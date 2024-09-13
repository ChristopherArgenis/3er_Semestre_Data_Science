def findsmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def selection_sort(arr):
  new_array = []
  for i in range(len(arr)):
    smallest = findsmallest(arr)
    new_array.append(arr.pop(smallest))
  return new_array

print(selection_sort([7, 3, 5, 9, 15, 13, 11, 2, 4, 17, 25, 22, 34, 45, 65, 32, 49, 78, 100, 98]))
# output: [2, 3, 4, 5, 7, 9, 11, 13, 15, 17, 22, 25, 32, 34, 45, 49, 65, 78, 98, 100]
print(selection_sort([17, 5, 2, 15, 6, 18, 12, 14, 7, 5, 15, 7, 6, 3, 14, 17, 4, 2, 13, 7]))
# output: [2, 2, 3, 4, 5, 5, 6, 6, 7, 7, 7, 12, 13, 14, 14, 15, 15, 17, 17, 18]