def listSorter(listToSort: ListToSort) -> ListToSort:
    for i in range(1, listToSort.Length() - 1):
        for j in range(0, listToSort.Length()-i):
            if listToSort.Larger(j, j+1):
                listToSort.Swap(j, j+1)
    return listToSort