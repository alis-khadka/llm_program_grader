def calc(n):
    def mul(b):
        if(b==0):
            return 1
        elif(b%2 == 0):
            a = mul(b//2)
            return (a*a) % 1000000007
        else:
            return (mul(b-1)*2 )% 1000000007
    n = n % 1000000007
    return (mul(n)-1) % 1000000007