def calc(A,B):
    C = [0 for i in range(len(B))]
    
    for i in range(len(A)):
        C[A[i]] += 1
    ret_str = ""
    for i in range(len(B)):
        if B[i] < C[i]:
            ret_str += '0'
        else: 
            ret_str += '1'
    return ret_str