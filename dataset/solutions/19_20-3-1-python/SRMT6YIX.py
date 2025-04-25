def partition(A: ListToSort, l, r):
    i = l-1
    for j in range(l,r):
        if not A.Larger(j,r):
            i = i + 1
            A.Swap(i,j)
    A.Swap(i+1,r)
    return i +1, A
    
def listSorter(listToSort: ListToSort, l = 0, r = None) -> ListToSort:
    if r is None:
        r = listToSort.Length() - 1
    if l < r:
        q, listToSort = partition(listToSort,l,r)
        listToSort = listSorter(listToSort, l, q-1)
        listToSort = listSorter(listToSort, q+1, r)
    return listToSort