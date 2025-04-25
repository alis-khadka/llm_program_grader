def calc(n):
    return (pow(2, n)-1) % 1000000007
    
# Die Folge entspricht der Formel a(n) = 2^n-1

def pow(a, b):
    if b == 0:
        return 1
    if b%2 == 0:
        c = b//2
        d = pow(a, c) % 1000000007
        return d * d
    else:
        c = b-1
        return pow(a, c) * a