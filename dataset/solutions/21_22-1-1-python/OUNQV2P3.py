def calc(n):
    return (powerOfTwo(n) - 1) % 1000000007

def powerOfTwo(n):
    if(n == 0):
        return 1
    if(n % 2 == 0):
        #even
        x = powerOfTwo(n//2) % 1000000007
        return x * x % 1000000007
    else:
        #odd
        return powerOfTwo(n - 1) * 2 % 1000000007