def calc(f):
    r = 1000000000000000000
    l = 0
    b = r-l+1
    return binarySearch(r,l,b)

def binarySearch(r,l,b):
    # nur eine Zahl übrig
    if b == 1:
        return l
    x = l + b//2 - 1
    # N ist kleiner gleich => links weitersuchen
    # bzw. Suchraum rechts verkleinern
    if f_N(x) == 1:
        r = x
    # N ist größer => rechts weitersuchen
    # bzw. Suchraum links verkleinern
    else:
        l = x + 1
    b = r-l+1
    return binarySearch(r,l,b)