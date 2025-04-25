def calc(A,B):
    for a in A:
        B[a] = B[a] - 1
    parts = []
    for b in B:
        if (b < 0):
            parts.append('0')
        else:
            parts.append('1')
    return "".join(parts)