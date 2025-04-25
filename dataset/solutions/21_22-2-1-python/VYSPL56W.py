def calc(A,B):
    out = ""
    
    c = [0] * (len(B))

    for i in A:
        c[i] += 1
    
    for x in range(len(B)):
        if c[x] <= B[x]:
            out = out + "1"
        else:
            out = out + "0"
    
    return out