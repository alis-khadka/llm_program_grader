def calc(a,b):
    for i in range(len(a)-1):
        a[i+1] += a[i]
    ans = []
    for i in range(len(b)):
        fr, to = b[i]
        r = a[to]
        if fr > 0:
            l = a[fr-1]
        else:
            l = 0
        ans.append(r-l)
    return ans