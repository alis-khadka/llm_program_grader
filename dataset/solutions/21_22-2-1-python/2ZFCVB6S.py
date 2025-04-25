def calc(A,B):
    m = len(B)
    n = len(A)
    C = {kategorie:0 for kategorie in range(m)}
    for i in range(n):
        C[A[i]] += 1
    s = ["1" if C[i] <= B[i] else "0" for i in range(m)]
    return "".join(s)