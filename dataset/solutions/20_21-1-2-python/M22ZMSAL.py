def solution(A, l=0, r=None):
    if r is None:
        r = len(A)-1
    if l<r:
        m = (l+r-1)//2
        solution(A, l, m)
        solution(A, m+1, r)
        merge(A, l, m, r)
    return A
def merge(A, l, m, r):
    div = m+1
    l_old = l
    arr = []
    for i in range(r-l+1):
        if l>m:
            arr.append(A[div])
            div = div+1
        elif div > r:
            arr.append(A[l])
            l+=1
        elif A[l]< A[div]:
            arr.append(A[l])
            l=l+1
        elif A[l]>= A[div]:
            arr.append(A[div])
            div +=1
    for i in range (len(arr)):
        A[i+l_old]=arr[i]