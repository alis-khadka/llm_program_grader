def listSorter(listToSort: ListToSort) -> ListToSort:
  last_unsorted_element = listToSort.Length()-1
  for _ in range(listToSort.Length()):
    for j in range(last_unsorted_element):
      if listToSort.Larger(j, j+1):
        listToSort.Swap(j, j+1)
  return listToSort