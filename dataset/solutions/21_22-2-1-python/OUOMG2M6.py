def calc(A,B):
    out = ['1']*len(B)
    for aᵢ in A:
        if B[aᵢ]:
            B[aᵢ] -= 1
        else:
           out[aᵢ] = '0'
           
    return ''.join(out)