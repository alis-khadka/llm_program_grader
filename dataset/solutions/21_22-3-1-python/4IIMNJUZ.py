def opt(W):
    b_in = 0
    b_ex = 0
    
    for e in W:
        new_b_ex = max(b_in,b_ex)
        
        b_in = b_ex + e
        b_ex = new_b_ex
    return max(b_ex,b_in)