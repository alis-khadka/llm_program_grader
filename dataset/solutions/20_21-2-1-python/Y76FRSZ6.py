def calc(A,B):
    counts = [0] * len(B)
    for a in A:
        counts[a] += 1
    s = ''.join('1' if count <= b else '0' for count, b in zip(counts, B))
    return s