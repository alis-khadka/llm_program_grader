def opt(W):
    best_incl = 0
    best_excl = 0

    for e in W:  # O(n)
        new_b_excl = max(best_excl, best_incl)

        best_incl = best_excl + e
        best_excl = new_b_excl

    return max(best_excl, best_incl)


assert opt([10, 2, 3, 4, 5]) == 18
assert opt([4, 9, 4]) == 9
assert opt([4, 7, 4]) == 8
assert opt([3, 2, 1]) == 4
assert opt([1, 2, 1, 4, 5]) == 7
assert opt([21, 2]) == 21
assert opt([5]) == 5
assert opt([30, 0, 0, 40]) == 70




def find_longest_path(s, v, graph, length):
    if (len(graph[v]) == 0):
        return length

    mx_len = 0

    for u in graph[v]:
        p = find_longest_path(s, u, graph, length+1)
        mx_len = max(mx_len, p)

    return mx_len