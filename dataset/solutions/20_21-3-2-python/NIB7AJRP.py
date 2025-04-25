def calc(N,A):
    adj = [[] for i in range(N + 1)] 
    for e in A:
        adj[e[0]].append(e[1])
    return findLongestPath(adj,N)

def dfs(node, adj, currentmpath, vis):  
    vis[node] = True 
    for i in range(0, len(adj[node])):   
        if not vis[adj[node][i]]: 
            dfs(adj[node][i], adj, currentmpath, vis)  
        currentmpath[node] = max(currentmpath[node], 1 + currentmpath[adj[node][i]])  
        
def findLongestPath(adj, n):  
    currentmpath = [0] * (n + 1)  
    vis = [False] * (n + 1) 
    for i in range(1, n + 1):   
        if not vis[i]:  
            dfs(i, adj, currentmpath, vis)  
    mpath = 0 
    for i in range(1, n + 1):   
        mpath = max(mpath, currentmpath[i])  
    return mpath