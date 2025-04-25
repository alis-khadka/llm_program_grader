def expo(a, b, c):
    if b == 0: return 1 % c
    elif b % 2 != 0: return (a * expo(a, b-1, c)) % c
    else:
        new_a = expo(a, b//2, c) % c
        return (new_a * new_a) % c
        
def calc(n):
    return expo(2, n, 1000000007) - 1