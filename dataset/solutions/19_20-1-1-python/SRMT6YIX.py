def LCM(a, b):
    if a < b:
        big, small = b, a
    else:
        big, small = a, b
    
    while (big % small):
        r = big % small
        big, small = small, r
    
    return (a*b)/small