def calc(f):
    N_max = 10 ** 18
    N_min = 1
    n = (N_max + N_min) // 2
    f_left_neighbour = f(n - 1)
    while f_left_neighbour is f(n):
        if f_left_neighbour:
            N_max = n - 1
        else:
            N_min = n + 1
        n = (N_max + N_min) // 2
        f_left_neighbour = f(n - 1)
    return n