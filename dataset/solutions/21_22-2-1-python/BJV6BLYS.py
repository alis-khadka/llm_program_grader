def calc(A,B):
    for i in A:
        B[i] = B[i]-1
    s = ""
    for i in B:
        if i <0 :
            s = s+"0"
        else: 
            s = s+"1"
    return s