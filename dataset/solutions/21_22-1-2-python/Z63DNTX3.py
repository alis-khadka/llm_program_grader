min_range = 0
max_range = 10**18
def calc(f):
    global max_range
    global min_range
    middle = (max_range + min_range)//2
    if middle == N:
        return middle
    if f(middle):
        max_range = middle+1
        return calc(f)
    else:
        min_range = middle
        return calc(f)