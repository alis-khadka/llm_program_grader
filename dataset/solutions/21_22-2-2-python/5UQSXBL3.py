def calc(a: list, b:list):
    n = len(a)
    c = [0]*n
    d = list()
    for i in range(0, n):
        c[i] += a[i] + c[i-1]
    for t in b:
        left = c[t[0]-1] if t[0] != 0 else 0
        d.append(c[t[1]]-left)
    return d