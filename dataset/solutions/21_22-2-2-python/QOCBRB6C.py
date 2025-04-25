def calc(a,b):

    l = [0] * len(b)
    s = {}
    s[-1] = 0

    for i in range(0, len(a)):
        s[i] = s[i-1] + a[i]


    for i in range(len(b)):
        l[i] = s[b[i][1]] - s[b[i][0]-1]


    return l