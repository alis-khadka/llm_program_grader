def calc(a,b):
    for i in range(1, len(a)): a[i] += a[i-1]
    return [a[r] if l == 0 else a[r]-a[l-1] for l,r in b]