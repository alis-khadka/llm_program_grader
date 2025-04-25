def calc(N,A):
    F = []
    P = []
    F.append(0)
    P.append(0)
    for n in range(1,N+1):
        F.append([])
        P.append([])
    for e in A:
        F[e[0]].append(e[1])
        P[e[1]].append(e[0])
    S = []
    AP = []
    AP.append(0)
    for i in range(1,len(P)):
        AP.append(len(P[i]))
        if AP[i] == 0:
            S.append(i)
    L = []
    L.append(S)
    i = 0
    while not len(L[i]) == 0:
        i+=1
        L.append([])
        for l in L[i-1]:
            for j in F[l]:
                AP[j]-=1
                if AP[j]==0:
                    L[i].append(j)
    return i-1