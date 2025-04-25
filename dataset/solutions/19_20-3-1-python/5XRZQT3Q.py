def listSorter(A: ListToSort) -> ListToSort:
    for i in range(0, A.Length()-1):
        # suche kleinstes Element aus A[i..N]
        min = i
        for j in range(i, A.Length()):
            if(A.Larger(min,j)):
                min = j
        # vertausche A[i] und A[min]
        A.Swap(min, i)
    return A