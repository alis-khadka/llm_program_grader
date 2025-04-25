def calc(f):
    left = 1
    right = 10**18
    
    while left < right:
        mid = left + (right-left) // 2
        if not f(mid):
            left = mid + 1
        else:
            right = mid

    return mid if f(mid) else mid + 1