def calc(f):
    return binSearch(0, 10**18, f)

def binSearch(left, right, f):
    mid = (left + right) // 2 
    if f(mid) == 1:
        if(f(mid - 1) == 0):
            return mid
        return binSearch(left, mid - 1, f)
    return binSearch(mid + 1, right, f)