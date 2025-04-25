def calc(N,A):

    lsg = [0]*N
    A.sort(key=sortkey)
    for i, k in enumerate(A):
        if lsg[k[1]-1] <= lsg[k[0]-1]:
            lsg[k[1]-1] = lsg[k[0]-1]+1


    return max(lsg)

def sortkey(e):
    return (e[1]*100 + e[0])