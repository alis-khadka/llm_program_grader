def calc(n):
    # Erkenne: wir berechnen hier 2^n-1 
    # Für gerade n gilt: 2^n = 2^(n/2) * 2^(n/2)
    cap = 1000000007
    return zweiHoch(n, cap) - 1

def zweiHoch(b, cap):
    if b == 0:
        # Terminierung bei 2^0 = 1
        return 1 
    elif b % 2:
        # ungerade, mit Hinweis 3
        res = 2 * zweiHoch(b-1, cap)
        return res % cap
    else:
        # gerade, mit Hinweis 3
        res = zweiHoch(b//2, cap)
        res = (res * res) % cap
        return res