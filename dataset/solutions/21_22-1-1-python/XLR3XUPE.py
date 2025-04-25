def binexp(a):
    y = 1; z = 2
    for x in "{0:b}".format(a)[::-1]:
        if x == "1":
            y *= z
        z *= z
    return y
    
def pow(a):
    return a * a
    
def squaremul(a):
    if a == 0:
        return 1
    
    if a == 1:
        return 2
        
    if a % 2 == 0:
        return pow(squaremul(a // 2)) % 1000000007
    
    if a % 2 == 1:
        return squaremul(a - 1) * 2 % 1000000007
        
        

def calc(a):
    
    return (squaremul(a) - 1) % 1000000007