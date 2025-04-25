def calc(a, b):
    s = [0] * len(b)
    c = [0] * len(b)
    for i in a:
        c[i] += 1
    for i in range(len(b)):
        if c[i] <= b[i]:
            s[i] = 1
    return ''.join(map(str, s))