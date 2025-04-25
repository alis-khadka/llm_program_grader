def calc(n):
    return ((binärExp(n) - 1) % (1000000000 + 7))


def binärExp(n):
    if n == 0:
        return 1 
    if n % 2 == 0:
        root = binärExp(n/2)
        return (root * root) % (1000000000 + 7)
    return (binärExp(n-1)  * 2) % (1000000000 + 7)