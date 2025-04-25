def calc(f):
    r=1000000000000000000
    l= 0;
    n= r //2;

    while(l!=r):
        if(f_N(n) == 0):
            l=n+1
            n= (l+r)//2
        else:
            r=n;
            n= (l+r)//2
    return r