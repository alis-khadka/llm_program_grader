def calc(N,A):
    knoten = {}
    for k in range(1,N+1):
        knoten[k] = []
    for k, a in A:
        knoten[k].append(a)
    marker = {}
    laenge = 0
    for k in range(1,N+1):
        pfad = laengsterPfad(marker,k,knoten)
        laenge = max(pfad,laenge)
    return laenge

def laengsterPfad(marker,k,knoten):
    pfad = 0
    for a in knoten[k]:
        if a not in marker:
            marker[a] = laengsterPfad(marker,a,knoten)
        pfad = max(pfad,marker[a]+1)
    return pfad