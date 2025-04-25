def calc(n):
    res = 1
    bs = 2
    while(n > 0):
        if ((n % 2) == 1):
            res =  (res * bs)  % 1000000007
        bs = (bs * bs) % 1000000007
        n = n //2
    return (res-1) % 1000000007