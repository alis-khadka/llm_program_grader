def listSorter(listToSort: ListToSort) -> ListToSort:
    for i in range (0,listToSort.Length()-1):
        noswap = True
        for j in range (listToSort.Length()-1,i,-1):
            if listToSort.Smaller(j,j-1):
                listToSort.Swap(j,j-1)
                noswap = False
        if noswap:
            break
    return listToSort