def dfs(node, ll, nodes_mp, min):
    if len(ll[node]) == 0:
        return 0
    elif nodes_mp[node] != min:
        return nodes_mp[node]
    else:
        bs = 0
        for child in ll[node]:
            bs = max(bs , dfs(child, ll, nodes_mp , min) + 1)
        nodes_mp[node] = bs
        return nodes_mp[node]

def calc(N,A):
    min=-10000
    ll = [[] for i in range(N + 1)]
    nodes_mp = [min] * (N + 1)
    ll[0] = [x for x in range(1, N + 1)]
    
    for edge in A:
        start=edge[0]
        end=edge[1]
        ll[start].append(end)
        
    return dfs(0, ll, nodes_mp, min) - 1