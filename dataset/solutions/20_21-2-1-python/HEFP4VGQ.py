def calc(A,B):
    result = ''
    for a in A:
        B[a] -= 1
    for b in B:
             result += '1' if b >= 0 else '0' 
    return result