def calc(f):
    lower = 0
    upper = 10**18
    while upper-lower > 1:
        middle = lower + (upper-lower)//2
        if f(middle) == 0:
            lower = middle
        else:
            upper = middle
    if upper-lower == 1:
        if f(lower) == 0:
            lower += 1
    return lower