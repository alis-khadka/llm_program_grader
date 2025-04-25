def expo(a: int, b: int, c: int) -> int:
    if not b:
        return 1 % c
    if b == 1:
        return a % c
    if b % 2:
        return expo(a, b-1, c) * expo(a, 1, c) % c
    else:
        res = expo(a, b // 2, c)
        return res*res % c