def calc(A,B):
    m=len(A)
    n=len(B)
    C=[0]*n
    fit_list=list()
    
    for i in range(m):
        C[A[i]]+=1
        
    for i in range(n):
        if C[i]>B[i]:
            fit_list.append(0)
        else:
            fit_list.append(1)
            
    result=''.join(map(str, fit_list))
    return result