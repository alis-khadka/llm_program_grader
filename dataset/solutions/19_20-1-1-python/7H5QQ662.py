def LCM(a: int, b: int) -> int:
    return (a * b) / GCD(a, b)

def GCD(a: int, b: int) -> int:
    if (a % b) == 0:
        return b
    return GCD(b, a % b)