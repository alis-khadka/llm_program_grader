def calc2(a: int, b: int) -> int:
    if b == 0:
        return 1
    else:
        if b % 2 == 0:
            b = b // 2
            half = calc2(2, b) % 1000000007
            return (half * half) % 1000000007
        else:
            b = b - 1
            minus_one = calc2(2, b) % 1000000007
            return (2 * minus_one) % 1000000007


def calc(n: int) -> int:
    if n == 0:
        return 0
    elif n < 0:
        return -1
    else:
        return calc2(2, n) % 1000000007 - 1