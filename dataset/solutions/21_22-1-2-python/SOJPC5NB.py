def calc(f):
    a=0
    b= 1000000000000000000-1
    while a<=b:
        mitte = (b+a)//2
        if f(mitte)==1:
            b=mitte-1
        else:
            a=mitte+1
    return a