def dfs(adj,n,maxp):
    if not maxp[n]:
        for i in adj[n]:
            dfs(adj,i,maxp)
            maxp[n] = max(maxp[n],1+maxp[i])

def calc(N,A) -> int : 
    adj = [[]for i in range(N)]
    for u,v in A:
        adj[u-1].append(v-1)
    
    maxp = [0 for i in range(N)]
    for n in range(N):
        
        dfs(adj,n,maxp)
            
    return max(maxp)