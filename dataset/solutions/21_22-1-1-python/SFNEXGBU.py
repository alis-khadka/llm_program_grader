def calc(n):
    n=int(n)
    d=[int(x) for x in bin(n)[2:][::-1]]
    return modexp(2, 1000000007,d)-1
    
def modexp(a , N, d):
    y = 1
    z = a % N
    for i in d:
        if i:
            y = y * z % N
        z = z*z % N
    return y