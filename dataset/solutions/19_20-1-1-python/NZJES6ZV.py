def GCD(a,b):
    if a<b:
        a,b=b,a
    while a%b>0:
        r=a%b
        a,b = b,r
    return b

def LCM(a, b):
    return (a*b)/GCD(a,b)