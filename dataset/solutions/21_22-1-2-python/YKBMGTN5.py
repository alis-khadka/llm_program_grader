def calc(f):
    return search(f, 0, 10**(18))
    
def search(f, a, b):
    if a == b:
        return a 
    
    if (b - a) == 1:
       return b if f(b) else a 

    else:
        l = a + int( (b-a)/2)
        if f(l) == 0:
            return search(f, l, b)
        
        else:
            return search(f, a, l)