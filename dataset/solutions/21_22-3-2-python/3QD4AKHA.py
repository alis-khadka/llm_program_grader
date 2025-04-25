def tiefenSuche(node, Adj, M):
    if len(Adj[node]) == 0:
        return 0
    elif M[node] != -1:
        return M[node]
    else:
        retVal = 0
        for i in range(0,len(Adj[node])):
            retVal =  max(retVal, tiefenSuche(Adj[node][i],Adj,M)+1)
        M[node] = retVal
        return M[node]

def calc(N,A):
    Adj = []
    for i in range(0,N+1):
        Adj.append([])
    Adj[0]=range(1,N+1)
    for j in A:
        Adj[j[0]].append(j[1])
    M = []
    for i in range(0,N+1):
        M.append(-1)
    return tiefenSuche(0,Adj,M)-1