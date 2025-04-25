def calc(N,A):
    Adj_list = [[] for _ in range(N)]
    for edge in A:
        Adj_list[edge[0] - 1].append(edge[1] - 1)
    paths = [0 for _ in range(N)]
    
    def path(steps, index):
        if paths[index] == 0:
            if Adj_list[index] == []:
                return steps
            buff = [0]
            for next in Adj_list[index]:
                buff.append(path(steps + 1, next))
            paths[index] = max(buff) - steps
        return paths[index] + steps
    
    for i in range(N):
        path(1, i)
    return max(paths)