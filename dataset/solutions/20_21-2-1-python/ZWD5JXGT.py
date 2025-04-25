# o(n + m)
def calc(A,B):
    # O(n)
    for a in A:
        B[a] -= 1
    
    # O(m)
    outstr = ""
    for i in range(0, len(B)):
        outstr += "1" if B[i] >= 0 else "0"
    
    return outstr