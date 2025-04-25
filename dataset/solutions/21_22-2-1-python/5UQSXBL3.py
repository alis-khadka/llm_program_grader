def calc(A: list, B: list) -> str:
    str_len = len(B)
    s = ''
    C = [0] * str_len
    
    for a in A:
        C[a] += 1    
    for b, c in zip(B, C):
        s += '1' if b >= c else '0'

    return s