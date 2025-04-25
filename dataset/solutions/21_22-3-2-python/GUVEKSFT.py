def calc(N,A):
    Knoten = []
    LP = []
    for e in range (N):
        Knoten.append([])
        LP.append(None)
    for i in range (len(A)):
        Knoten[A[i][1]-1].append(A[i][0])
    maxPfad(Knoten,LP,N,0)
    return(max(LP))


def maxPfad(Knoten,LP,N,s):
    if (len(Knoten[s]) == 0):
        LP[s] = 0
        if (s < N-1):
            maxPfad(Knoten,LP,N,s+1)
    else:
        maxi = 0
        for i in range (len(Knoten[s])):
            if (LP[Knoten[s][i]-1] != None and LP[Knoten[s][i]-1] >= maxi):
                maxi = LP[Knoten[s][i]-1] + 1
                LP[s] = maxi
        if (s < N-1):
            maxPfad(Knoten,LP,N,s+1)