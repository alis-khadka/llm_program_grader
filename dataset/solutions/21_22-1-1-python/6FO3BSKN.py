def temp(n):
    if n ==0:
        return 1
    elif n % 2 == 0:
        even = temp(n//2)
        return even * even % 1000000007
    else:
        odd = (temp(n//2))
        return odd * odd * 2 % 1000000007

def calc(x):
    return temp(x)-1