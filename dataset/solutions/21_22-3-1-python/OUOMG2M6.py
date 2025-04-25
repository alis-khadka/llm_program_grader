from collections import defaultdict


def opt(xs):
    L    = len(xs) - 1
    W    = defaultdict(int)
    for i, v in enumerate(reversed(xs)):
        W[L - i] = v + max(W[L - i + 2], W[L - i + 3])

    return max(W.values())