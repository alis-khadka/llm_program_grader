def listSorter(listToSort: ListToSort) -> ListToSort:
    for i in range(listToSort.Length()):
        for j in range(listToSort.Length()):
            if listToSort.Smaller(i,j):
                listToSort.Swap(i,j)
    return listToSort