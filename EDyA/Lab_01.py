# Python 3 program for recursive binary search.
def binary_search(lista, item):
  low = 0
  high = len(lista) - 1

  while low <= high:
    mid = (low + high)//2
    guess = lista[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None

my_list = range(20)

print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None