def opt(W):
    n=len(W)-1
    o=[]
    for i in range(0,n+1):
        o.append(0)
    o[0]=W[0]    
    if W[0] < W[1]:
        o[1] = W[1]
    else:
        o[1] = W[0]
    for i in range(2,n+1):
        o[i]=max(o[i-1],o[i-2]+W[i])
    return o[n]