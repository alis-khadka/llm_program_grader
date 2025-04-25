def calc(A,B):
    s = [0] * len(B)
    mem = [0] * len(B)
    for a in A:
        mem[a] += 1
    for i in range(0,len(B)):
        if mem[i] <= B[i]:
            s[i] = 1
    return ''.join([str(i) for i in s])