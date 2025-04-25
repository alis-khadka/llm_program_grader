def calc(A: list,B: list):
    c = [0] * len(B)
    
    for a in A:
        c[a] += 1
        
    result = ""
    
    for i,b in enumerate(B):
        result += str(int(c[i]<= b))
        
    return result