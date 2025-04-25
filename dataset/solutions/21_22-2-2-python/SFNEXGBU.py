def calc(A,B):
    output = []
    d = [0]
    for i,a in enumerate(A):
        d += [a+d[i]]
    
    for i,t in enumerate(B):
        l = t[0]
        r = t[1]+1
        output += [d[r]-d[l]]
        
    return output