def calc(f):
    mid = -1
    lower = 1
    upper = 1000000000000000000
    
    while(upper - lower > 1):
        mid = (upper + lower) // 2
        if (f(mid) == 1):
            upper = mid
        else:
            lower = mid
    if (f(lower) == 1):
        return lower
    return upper