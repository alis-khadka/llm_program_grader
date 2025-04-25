def expo(a,b,c):
    i=1
    ergebnis = 1
    a=a%c
    while(b>0):
        if((b&1)==1):
            ergebnis = (ergebnis*a)%c
        b = b >> 1    
        a = (a*a)%c
        i += 1
    return ergebnis    
