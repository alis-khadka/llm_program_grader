def calc(n, tree):
    weight = [None for _ in range(n)]
    
    neigh = [[] for _ in range(n)]
    for edge in tree:
        neigh[edge[0]-1].append(edge[1]-1)

    s = []

    for u in range(n):
        if weight[u] is None:
            s.append(u)
            while s != []:
                v = s[-1]
                if not neigh[v]:  # can be made shorter, will be slightly slower then.
                    weight[v] = 0
                    s.pop()
                elif all([not weight[i] is None for i in neigh[v]]):
                    weight[v] = 1 + max([weight[i] for i in neigh[v]])
                    s.pop() 
                else:
                    for kid in neigh[v]:
                        if weight[kid] is None:
                            s.append(kid)
    return max(weight)