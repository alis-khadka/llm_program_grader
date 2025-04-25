def calc(A,B):
    
    Ai = []
    s = ''
    
    for i in range(len(B)):
        Ai.append(0)
    
    for k in A:
        Ai[k] = Ai[k] + 1
    
    for j in range(len(B)):
        if Ai[j] > B[j]:
            s = s + '0'
        else:
            s = s + '1'
    
    return s