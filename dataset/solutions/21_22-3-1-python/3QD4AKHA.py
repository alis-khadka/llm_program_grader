def maximum(a,b):
    if a>b : return a
    else   : return b


def opt(W):
    M = [W[0]]
    n = len(W)
    if W[0] < W[1]:
        M.append(W[1])
    else:
        M.append(W[0])
    for i in range(2, n):
        M.append(maximum(M[i-1],W[i]+M[i-2]))
    
    return M[n-1]