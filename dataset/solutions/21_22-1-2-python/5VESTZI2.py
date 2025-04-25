def calc(f):
    a = 0
    b = 10**18
    x = (a+b)//2
    val = f(x)
    for i in range(60):
        if val == 0:
            a = x
        else:
            b = x
        x = (a+b)//2
        val = f(x)
    return x + 1