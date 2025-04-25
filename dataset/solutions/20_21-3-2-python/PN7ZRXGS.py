def calc(N, A):

    length = [0]*(N+1)

    edges = {new_list: [] for new_list in range(N+1)}
    for a in A:
        end = a[1]
        edges[end].append(a)

    for n in range(N+1):
        for i in edges[n]:
            if(length[i[0]]+1>length[n]):
                length[n] = length[i[0]]+1
    return max(length)