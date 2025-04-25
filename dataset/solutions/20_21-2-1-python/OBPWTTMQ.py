def calc(A,B):
    d = dict()
    for cat in A:
        if not cat in d:
            d[cat] = 1
        else:
            d[cat] += 1
    s = ""
    for cat in range(len(B)):
        if not cat in d:
            s += "1"
        elif B[cat] < d[cat]:
            s += "0"
        else:
            s += "1"
    return s