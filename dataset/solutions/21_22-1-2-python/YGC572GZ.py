def calc(f):
    max = 10**18
    min = 0
    while (max != min):
        m= (max - min)//2  +min
        if(f(m)==0):
            min = m +1
        else:
            max = m 
    return max