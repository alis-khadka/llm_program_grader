def calc(N,A):
    Lengths = []
    Connections = []

    for i in range(N):
        Lengths += [0]
        Connections += [[]]

    for e in A:
        assert e[0] < e[1]
        Connections[e[0]-1] += [e[1]-1]

    for e in range(len(Connections)):
        for u in Connections[e]:
            Lengths[u] = max(Lengths[e] + 1, Lengths[u])

    return max(Lengths)