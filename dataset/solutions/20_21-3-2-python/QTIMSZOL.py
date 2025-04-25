nodes = []  # list of Node instances
adj = []  # adjacency list; list of node i is at position i-1
time = 0  # timestamp for dfs
top = []  # reverse topological sort of Node instances


class Node:
    WHITE = 0
    BLACK = 1

    def __init__(self, id):
        self.id = id
        self.color = Node.WHITE
        self.pi = None
        self.d = None
        self.f = None


def dfs_visit(u):
    global time
    time += 1
    u.d = time
    for v in adj[u.id - 1]:
        if v.color == Node.WHITE:
            v.pi = u
            dfs_visit(v)
    u.color = Node.BLACK
    time += 1
    u.f = time
    top.append(u)


def calc(N, E):
    global nodes, adj
    # create list of nodes
    for u in range(N):
        nodes.append(Node(u + 1))

    # build adjacency list
    adj = [[] for _ in range(N)]
    for e in E:
        adj[e[0] - 1].append(nodes[e[1] - 1])

    # DFS
    for u in nodes:
        if u.color == Node.WHITE:
            dfs_visit(u)

    res = [0] * N

    for u in top:
        if adj[u.id - 1]:
            res[u.id - 1] = max([res[v.id - 1] for v in adj[u.id - 1]]) + 1

    return max(res)