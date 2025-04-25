def calc(f):
    left = 1
    right = 10**18
    f_return = 0
    while 0 <= left <= right:
        mid = (right + left) // 2
        
        f_return = f(mid)
        
        if f_return == 1:
            right = mid - 1
        else:
            left = mid + 1
            
    if f_return == 1:
        return mid
    else:
        return mid + 1