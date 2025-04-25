def calc(N,A):

    cld = {}
    p = {}
    T = {}

    for e in A:
        a = e[0]
        b = e[1]
        if a not in cld:
            cld[a] = []
        if a not in T:
            T[a] = 0
        if a not in p:
            p[a] = []
        if b not in cld:
            cld[b] = []
        if b not in T:
            T[b] = 0
        if b not in p:
            p[b] = []
        p[b].append(a)
        cld[a].append(b)

    cn = {}
    for i in cld:
        cn[i] = len(cld[i])
    oc = {}
    for i in range(-1, N):
        oc[i] = []
    for i in cn:
        oc[cn[i]].append(i)
    #print(cn)
    #print(oc)

    #print(p)
    #print(cld)

    while len(oc[0]) != 0:
        leaf = oc[0][0]
        tl  = T[leaf]
        #print("looking at leaf {} with max depth {}".format(leaf, T[leaf]))
        for parent in p[leaf]:
            pc = cn[parent]
            oc[pc].remove(parent)
            oc[pc-1].append(parent)
            cn[parent] = pc-1
            T[parent] = max(T[parent], tl + 1)
        oc[0].remove(leaf)


    return (max(T.values()))