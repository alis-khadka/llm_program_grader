def solution(A):
    def merge(xs, ys):
        zs = []
        while xs and ys:
            if xs[0] <= ys[0]:
                zs.append(xs.pop(0))
            else:
                zs.append(ys.pop(0))
        return zs + xs + ys
    l = len(A)
    if l > 1:
        return merge(solution(A[:l//2]), solution(A[l//2:]))
    else:
        return A