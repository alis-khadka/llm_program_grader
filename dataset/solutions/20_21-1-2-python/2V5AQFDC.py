def solution(A):
    if len(A) < 2:
        return A
    fertig = []
    mid = int(len(A) / 2)
    rechts = solution(A[:mid])
    links = solution(A[mid:])
    while (len(rechts) > 0) and (len(links) > 0):
        if rechts[0] > links[0]:
            fertig.append(links[0])
            links.pop(0)
        else:
            fertig.append(rechts[0])
            rechts.pop(0)
    fertig += rechts
    fertig += links
    return fertig