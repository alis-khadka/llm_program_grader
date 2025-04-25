def calc(f) -> int:
    low = 1
    high = 1e18
    mid = high // 2
    while low != high:
        if f(mid) == 1:
            high = mid
        else:
            low = mid + 1
        mid = int((low + high) // 2)
    return low