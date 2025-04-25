def calc(f):
    l = 0
    r = pow(10, 18)
    
    while 0 <= l <= r:
        mid = (l+r) // 2
        
        if f(mid) == 0:
            l = mid + 1
        else:
            r = mid - 1
            
    if f(mid) == 0: return mid + 1
    else: return mid