def calc(n):
    n = int(n)
    if n<=2:
        p = pow(2,n)-1
        return(p%1000000007)
    else :
        if n%2 == 1:
            R = 1
            n = (n-1)//2
            c = calc(n)+1
            c = pow(c,2)%1000000007
            res = (2*c)%1000000007
            return(res-1)
        else:
            n = n//2
            c = calc(n)+1
            res = pow(c,2)%1000000007
            return(res-1)
    pass