def _(a: int , N: int, d: [int]):
    y = 1
    z = a % N
    for i in d:
        if i:
            y = y * z % N
        z = z*z % N
    return y



def calc(n):
    n = bin(int(n))[2:][::-1]
    A = _(2, 1000000007, list(map(int, n)))
    return A - 1