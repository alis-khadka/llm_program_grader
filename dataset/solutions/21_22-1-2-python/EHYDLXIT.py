def calc(f):
    return binary(0,1000000000000000000,f)


def binary(l,r,f):
    mid = l + (r-l) //2
    
    if (f(mid) == 1 and f(mid-1) == 0 and f(mid+1) == 1):
        return mid
    
    if (f(mid) == 1):
        return binary(l,mid-1,f)
    else:
        return binary(mid+1,r,f)