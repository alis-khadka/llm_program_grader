def calc(A,B):
    maxi = max(A)
    C = [0] * (maxi + 1)
    for i in range(len(A)):
        C[A[i]] += 1 

    stri = ""    

    for i in range(len(B)):
        if(i>maxi or C[i]<=B[i]):
            stri += "1"
        else:
            stri += "0"
    return stri