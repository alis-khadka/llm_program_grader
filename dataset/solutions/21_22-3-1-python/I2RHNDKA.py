def opt(W):
    A=W
    for i in range(len(A)):
        if i==0:
            continue
        elif i==1:
            if A[i-1]>A[i]:
                A[i]=A[i-1]
        elif A[i]+A[i-2]>A[i-1]:
            A[i] += A[i-2]
        else:
            A[i]=A[i-1]
    return A[-1]