class KnotenImKopf:
    def __init__(self, wert: int):
        self.wert = wert
        self.farbe = "w"
        # self.vater = None
        # self.d = None
        # self.f = None
        self.adj = []

    def append_to_adj(self, wert: int) -> None:
        self.adj.append(wert)


def dfs(knoten: list) -> list:
    # global zeit
    # zeit = 0
    endzeit_list = []

    for u in knoten[1:]:  # s. Init. von knoten
        if u.farbe == "w":
            dfs_visit(knoten, u, endzeit_list)
    return endzeit_list


def dfs_visit(knoten: list, u: KnotenImKopf, endzeit_list: list) -> None:
    # global zeit
    # zeit += 1
    # u.d = zeit
    u.farbe = "g"
    for v_value in u.adj:
        v = knoten[v_value]
        if v.farbe == "w":
            # v.vater = u.wert
            dfs_visit(knoten, v, endzeit_list)
    # u.farbe = "s"
    # zeit += 1
    # u.f = zeit
    endzeit_list.append(u.wert)


def calc(n: int, a: list) -> int:
    knoten = [KnotenImKopf(i) for i in range(n + 1)]  # 0-ter Knoten ist PLatzhalter
    for e in a:
        knoten[e[0]].append_to_adj(e[1])
    e_list = dfs(knoten)
    longest_path = [0] * (n + 1)

    for value in e_list:
        u = knoten[value]
        for v in u.adj:
            longest_path[value] = max(longest_path[value], longest_path[v] + 1)

    return max(longest_path)