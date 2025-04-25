def calc(n):
    return squaremultiply(n)-1
    
def squaremultiply(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        x = squaremultiply(n/2)
        return (x * x ) % 1000000007
    else:
        return 2 * squaremultiply(n-1) % 1000000007