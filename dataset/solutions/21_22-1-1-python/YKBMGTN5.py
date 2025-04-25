N = 1000000007

def calc(n):
    n = int(n)
    if n == 0:
        return 0
    
    else:
        d = bin(n)[:1:-1]
        return (modexp(d) - 1) % N
    
def modexp(d):
    y = 1
    z = 2 % N
    
    for i in range(len(d)):
        if d[i] == '1':
            y = (y * z) % N
        z = (z * z) % N
    
    return y