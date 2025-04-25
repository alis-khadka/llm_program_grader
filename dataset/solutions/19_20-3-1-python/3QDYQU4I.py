def listSorter(listToSort: ListToSort) -> ListToSort:
    
    # selection sort
    
    # laziness
    l = listToSort
    
    # why can't ListToSort just work with len() and why is .Length() capitalized?
    for i in range (0,l.Length()):
        
        # find minimum in l[i,]
        mini = i
        for j in range(i+1, l.Length()):
            if l.Smaller(j,mini):
                mini = j
                
        # swap minimum to the left
        l.Swap(mini, i)
    
    return l