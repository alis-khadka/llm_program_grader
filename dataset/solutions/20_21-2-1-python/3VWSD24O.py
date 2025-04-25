def calc(A,B):
    categ = dict()
    for a in A:
        if not (a in categ):
            categ[a] = 0
        categ[a] += 1
        
    s = ''
    
    for i in range(len(B)):
        if not (i in categ):
            s += '1' 
        elif categ[i] > B[i]:
            s += '0'
        else:
            s += '1'
    return s