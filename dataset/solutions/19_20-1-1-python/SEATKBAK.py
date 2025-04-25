def gcd(a,b):
    #make sure a > b
    (a,b) = sorted([a,b],reverse= True)
    #recursive algorithm
    if a%b == 0:
        return b
    else:
        (a,b) = (b, a%b)
        return gcd(a,b)
        
def LCM(a, b):
    
    return a*b/ gcd(a,b)