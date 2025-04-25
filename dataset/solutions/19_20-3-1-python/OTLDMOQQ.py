def partition(A, l, r):
    i = l-1
    j = r
    while i < j:
        i+=1
        while A.Larger(r, i):
            i+=1
        j-=1
        while A.Smaller(r, j):
            j+=1
        if i < j:
            A.Swap(i, j)
    A.Swap(i, r)
    return i

def quicksort(A, l, r):
    if l < r:
        q = partition(A, l, r)
        quicksort(A, l, q-1)
        quicksort(A, q+1, r)

def listSorter(listToSort: ListToSort) -> ListToSort:
    l = 0
    r = listToSort.Length() - 1
    quicksort(listToSort, l, r)
    return listToSort