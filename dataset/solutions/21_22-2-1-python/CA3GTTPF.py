def calc(A,B):
    c=[0] * len(B)
    for i in A:
        c[i] += 1
    s=""
    for(i,cap) in enumerate(B):
        if c[i] > cap:
            s+="0"
        else:
            s+="1"
    return s