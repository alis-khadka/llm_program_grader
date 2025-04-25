def calc(n):

    n_int = int(n) % 1000000007

    split = 512

    if n_int == 0:
        return 0

    mod = n_int % split

    n_gerade = (n_int-mod)//split
    return (pow(pow(2,n_gerade) % 1000000007, split) * pow(2, mod) - 1) % 1000000007