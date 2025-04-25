def listSorter(listToSort: ListToSort) -> ListToSort:
    for i in range(listToSort.Length()-1):
        for j in range(listToSort.Length()-1-i):
            if listToSort.Larger(j,j+1):
                listToSort.Swap(j,j+1)
    return(listToSort)