def listSorter(listToSort: ListToSort) -> ListToSort:
    for i in range(0,listToSort.Length()):
        min = i
        for j in range(i+1,listToSort.Length()):
            if listToSort.Smaller(j,min):
                min = j
        listToSort.Swap(min,i)
    return(listToSort)