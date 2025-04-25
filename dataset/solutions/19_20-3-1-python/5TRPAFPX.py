def listSorter(listToSort: ListToSort) -> ListToSort:
    return myQuicksort(listToSort, 0, listToSort.Length()-1)
    
def myQuicksort(listToSort, l, r):
    if r-l > 0:
        p = partition(listToSort, l, r)
        myQuicksort(listToSort, l, p-1)
        myQuicksort(listToSort, p, r)
    return listToSort
    
def partition(listToSort, l, r):
    p = r
    while l < r:
        while listToSort.Smaller(l, p) or (listToSort.Equal(l, p) and l < r):
            l = l+1
        while listToSort.Larger(r, p) or (listToSort.Equal(r, p) and l < r):
            r = r-1
            if r < 0:
                break
        if l < r:
            listToSort.Swap(l, r)
    listToSort.Swap(l, p)
    return l