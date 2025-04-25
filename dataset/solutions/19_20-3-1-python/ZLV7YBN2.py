def listSorter(listToSort: ListToSort) -> ListToSort:
    for i in range(0,listToSort.Length()):
        for j in range(0,listToSort.Length()):
            if listToSort.Smaller(i,j):
                listToSort.Swap(i,j)
    return listToSort