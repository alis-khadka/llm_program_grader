def listSorter(listToSort: ListToSort) -> ListToSort:
    quicksort(listToSort, 0, listToSort.Length()-1)
    return listToSort

def quicksort(listToSort, l, r):
    if l < r:
        q = partition(listToSort, l, r)
        quicksort(listToSort, l, q-1)
        quicksort(listToSort, q+1, r)

def partition(listToSort, l, r):
    i = l-1
    j = r

    while i < j:
        i += 1
        while listToSort.Smaller(i, r):
            i += 1

        jGreaterPivot = True
        while jGreaterPivot:
            if j > 0:
                j -= 1
                jGreaterPivot = listToSort.Larger(j, r)
            else:
                break
                
        if i < j:
            listToSort.Swap(i, j)

    listToSort.Swap(i, r)
    return i