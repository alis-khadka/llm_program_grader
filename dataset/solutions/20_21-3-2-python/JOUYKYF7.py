def calc(N, A):
    visited = set()
    table = [0] * (N + 1)
    adj = dict()
    for e in A:
        if e[0] in adj:
            adj[e[0]].append(e[1])
        else:
            adj[e[0]] = [e[1]]
    for v in range(1, N + 1):
        if v not in visited:
            helper(v, adj, table, visited)
    count = 0
    for i in range(1, N + 1):
        count = max(count, table[i])
    return count


def helper(v, adj, table, visited):
    visited.add(v)
    try:
        for w in adj[v]:
            if w not in visited:
                helper(w, adj, table, visited)
            table[v] = max(table[v], table[w]+1)
    except KeyError:
        pass