def calc(N,A):
    length_to = [0 for x in range(N)]
    verts = {}
    for x in range(N):
        verts[x] = []

    for i in A:
        v = i[0] - 1
        verts[v].append(i)

    for v in range(N):
        edges = verts[v]
        for edge in edges:
            w = edge[1] - 1

            if length_to[w] <= length_to[v] + 1:
                length_to[w] = length_to[v] + 1
        
    return max(x for x in length_to)