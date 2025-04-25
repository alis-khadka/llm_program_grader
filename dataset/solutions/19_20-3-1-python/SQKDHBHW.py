def listSorter(listToSort: ListToSort) -> ListToSort:
    quickSort(listToSort, 0, listToSort.Length() - 1)
    return listToSort

def quickSort(listToSort: ListToSort, l: int, r: int):
    if l < r:
        q = partition(listToSort, l, r)
        quickSort(listToSort, l, q - 1)
        quickSort(listToSort, q + 1, r)
    
def partition(listToSort: ListToSort, l: int, r: int):
  i = l - 1
  j = r
  while i < j:
      while True:
        i += 1
        if not listToSort.Smaller(i, r):
          break
      while True:
        j -= 1
        if not listToSort.Larger(j, r) or j == 0:
          break
      if i < j:
          listToSort.Swap(i, j)
  listToSort.Swap(i, r)
  return i