def calc(A,B):
    C = [0]*(len(B))
    for a in A:
        C[a] +=1
    output = ''
    for i in range(0,len(B)):
        if C[i] <= B[i]:
            output += '1'
        else:
            output += '0'
    return output