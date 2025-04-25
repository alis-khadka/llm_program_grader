def calc(N,A):
    zahler = 0
    d = [0] * N
    kp = []
    A = sorted(A, key=lambda x:x[0])
    for entry in A:
        d[entry[1]-1] = max(d[entry[0]-1]+1 , d[entry[1]-1])

    return max(d)