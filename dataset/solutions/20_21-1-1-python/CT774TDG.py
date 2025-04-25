def expo(a: int, b: int, c: int) -> int:
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b == 2:
        return a * a
    elif b % 2 == 0:
        return expo(expo(a, b//2, c), 2, c) % c
    else:
        return a * expo(expo(a, (b-1)//2, c), 2, c) % c
