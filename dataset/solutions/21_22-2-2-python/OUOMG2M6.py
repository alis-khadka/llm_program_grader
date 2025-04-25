from itertools import accumulate

def calc(A,B):
    lookup = [0] + list(accumulate(A))
    return [lookup[rᵢ + 1] - lookup[lᵢ] for (lᵢ, rᵢ) in B]