def calc(f_N):
    lower = 0
    upper = pow(10,18)
    N = 0
    abb = bool(True)
    while abb:
        mid = lower+(upper-lower)//2
        if f_N(mid)==0:
            lower = mid
        else:
            if f_N(mid-1) == 0:
                N=mid
                return N
                abb = bool(False)
            else:
                upper = mid