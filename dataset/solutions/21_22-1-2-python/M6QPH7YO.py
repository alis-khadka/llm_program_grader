def calc(f):
    l = 0
    r = 10**(18)
    while True:
        mid = (l+r)//2
        if(f(mid-1)== 0 and f(mid)==1):
            return mid
            
        if(f(mid )==0):
            l = mid+1
        else:
            r = mid