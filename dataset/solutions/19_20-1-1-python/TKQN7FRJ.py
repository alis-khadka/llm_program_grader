def GCD(a, b):
    while b!=0:
        c=a%b
        a=b
        b=c
    return a

def LCM(a, b):
    return (a*b)/GCD(a,b)