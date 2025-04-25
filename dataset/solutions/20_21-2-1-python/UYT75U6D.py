def calc(A,B):
    C = [0]*len(B)
    text = []
    for kat in A:
        C[kat] = C[kat] + 1
    for x in range(len(B)):
        text.append('1') if (C[x] <= B[x]) else text.append('0')
    return ''.join(text)