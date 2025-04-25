def calc(N,A):
    V={}
    for i in range(1,N+1):
        V[i]=[]
    for edge in A:
        V[edge[0]].append(edge) 
         
    LP=[] 
    for i in range(0,N+1):
        LP.append(-1)
    for i in range(1,N+1):
        opt(i,V,LP)
    
    l = 0
    for num in LP:
        if l < num:
            l=num
    return l

def opt(i,V,LP):
    if LP[i] <0:
        if V[i]:
            for edge in V[i]:
                a=1+opt(edge[1],V,LP)
                if a > LP[i]:
                    LP[i] =a
            return LP[i]
                
        else:
            LP[i]=0
            return LP[i]
    else:
        return LP[i]