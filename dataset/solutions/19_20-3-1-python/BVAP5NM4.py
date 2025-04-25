def listSorter(listToSort: ListToSort) -> ListToSort:
    for i in range(listToSort.Length()):
        _min = i
        for j in range(i+1, listToSort.Length()):
            if listToSort.Smaller(j, _min):
                _min = j
        listToSort.Swap(i, _min)
    return listToSort