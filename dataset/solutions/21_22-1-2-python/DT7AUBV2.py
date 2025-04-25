def calc(f):
    a = 0
    b = 10**18
    
    while b-a >= 2:
        p = (a+b) // 2
        if f(p) == 0:
            a = p
        else:
            b = p
            
    return b