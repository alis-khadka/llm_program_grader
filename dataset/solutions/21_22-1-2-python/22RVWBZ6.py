def calc(f):
    j = 0
    lim1 = 0
    lim2 = int(1e+18)
    while j == 0:
        pivo = (lim1+lim2)//2
        if f(pivo):
            lim2 = pivo
            if lim1 == lim2:
                j = 1
        else:
            lim1 = pivo+1
            if lim1 == lim2:
                j = 1
    return lim1