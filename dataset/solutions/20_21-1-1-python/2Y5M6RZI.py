def expo(a, b, c):
    j=b
    res=1
    res1=a%c
    
    while j>0:
        if j%2!=0:
            res=(res1*res)%c
            j-=1
        res1=(res1*res1)%c
        j=j/2

    return res
