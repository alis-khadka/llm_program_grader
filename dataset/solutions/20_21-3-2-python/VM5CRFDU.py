def DFS_Visit(adj,u,times,colour):
    colour[u] = 'g'
    for v in adj[u]:
        if colour[v] == 'w':
            times, colour = DFS_Visit(adj,v,times,colour)
    colour[u] = 's'
    times.append(u)
    return times, colour

def DFS(adj):
    colour = dict()
    times = list()
    for u in adj:
        colour[u] = 'w'
    for u in adj:
        if colour[u] == 'w':
            times, colour = DFS_Visit(adj,u,times,colour)
    return times
        
def calc(N,A):
    adj = dict()
    for u in range(1,N+1):
        adj[u] = list()
    for e in A:
        adj[e[0]].append(e[1])
    times = DFS(adj)
    order = [u for u in reversed(times)]
    dist = dict()
    for u in order:
        dist[u] = 0
    for u in order:
        for v in adj[u]:
            dist[v] = max(dist[u]+1,dist[v])
    values = list(dist.values())
    return max(values)