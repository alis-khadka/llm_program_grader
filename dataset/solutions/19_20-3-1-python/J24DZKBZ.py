def listSorter(listToSort: ListToSort) -> ListToSort:
    for i in range (listToSort.Length()):
        min = i
        #print('i is {}'.format(i))
        for j in range (i+1,listToSort.Length()):
            if listToSort.Smaller(j,min):
                #print ('{} is smaller than {}'.format(j,min))
                min = j
                #print ('min now is {} '.format(min))
        #print('{} will now be swapped with {}'.format(i,min))
        if not (listToSort.Equal(i,min)):
            listToSort.Swap(i,min)
    return (listToSort)