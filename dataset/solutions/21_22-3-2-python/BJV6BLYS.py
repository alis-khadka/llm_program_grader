def calc(N,A):
    
    adj=[[] for i in range(N+1)]
    for u,v in A:
        adj[u].append(v)
    
    path = [0] * (N + 1) #Array für Pfadlänge
    visited = [False] * (N + 1) #Knoten besucht
    longestpath = 0

    for i in range(1, N + 1): 
        if not visited[i]:
            dfs(i, adj, path, visited) #Tiefensuche an unbesuchten Knoten
   
    for i in range(1, N + 1): 
        longestpath = max(longestpath, path[i]) #längsten Pfad finden
      
    return longestpath

def dfs(node, adj, path, visited):

    visited[node] = True
 
    for i in range(0, len(adj[node])): 

        if not visited[adj[node][i]]:
            dfs(adj[node][i], adj, path, visited)

        path[node] = max(path[node], 1 + path[adj[node][i]])