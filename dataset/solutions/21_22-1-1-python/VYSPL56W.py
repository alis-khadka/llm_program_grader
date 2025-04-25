def calc(n):
    n = int(n)
    if n == 0:
        return 0
    else:
        help = pow_mod(2, n, 1000000007)
        return (help + n - (n + 1))



def pow_mod(b, e, m):
    if e == 0:
        return 1
    elif e == 1:
        return b % m
    else:
        root = pow_mod(b, e // 2, m)
        if e % 2 == 0:
            return (root * root) % m
        else:
            return (root * root * b) % m