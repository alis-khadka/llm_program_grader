def calc(f):
    min = 1
    max = 10**18
    
    while(min != max):
        #print(str(min) + ", " + str(max))
        mid = (min + max)//2
        if(f(mid)):
            #N >= mid ==> new range mid, max
            max = mid
        else:
            #N < mid ==> new range min, mid
            min = mid + 1
    return min