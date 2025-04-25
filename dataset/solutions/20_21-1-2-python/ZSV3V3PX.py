def merge(A, B):
    a = b = 0
    C = []
    while (a < len(A) or b < len(B)):
        if (a < len(A) and b < len(B)):
            if (A[a] <= B[b]):
                C.append(A[a])
                a += 1
            else:
                C.append(B[b])
                b += 1
        elif (a < len(A) and b >= len(B)):
            C.append(A[a])
            a += 1
        else:
            C.append(B[b])
            b += 1
    return C

def solution(A):
    if (len(A) <= 1):
        return A
    else:
        return merge(solution(A[:len(A)//2]), solution(A[len(A)//2:]))