def LCM(a, b):
    if a > b:
        gr = a
        sma = b
    else:
        gr = b
        sma = a

    while sma > 0:
        tmp = gr % sma
        gr = sma
        sma = tmp

    kgV = a * b / gr
    return kgV