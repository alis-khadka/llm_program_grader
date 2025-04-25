def listSorter(listToSort: ListToSort) -> ListToSort:
    for i in range(0, listToSort.Length()-1):
        min = i
        for j in range(i, listToSort.Length()):
            if(listToSort.Larger(min,j)):
                min = j
        listToSort.Swap(min, i)
    return listToSort