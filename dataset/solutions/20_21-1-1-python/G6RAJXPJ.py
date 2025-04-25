def expo(a,b,c):
    ergebnis = 1
    while b != 0:
        if b & 1:
            ergebnis = (ergebnis * a) % c
        b >>= 1
        a = (a * a) % c
    return ergebnis
