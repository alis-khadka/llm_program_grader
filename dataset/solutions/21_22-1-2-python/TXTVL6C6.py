def calc(f):
    left = 0
    right = 10**(18)
    middle = (left + right) // 2
    while f(middle) == f(middle - 1):
        if f(middle) == 0:
            left = middle
            middle = (left + right) // 2
        else:
            right = middle
            middle = (left + right) // 2
    return int(middle)