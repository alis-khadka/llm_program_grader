def calc(n):
    mod_op = 1000000007
    x = 2
    res = 1
    while (n):
        if (n % 2):
            res = (res * x) % mod_op
        x = (x * x) % mod_op
        n = n // 2
    res = (res - 1) % mod_op
    return res