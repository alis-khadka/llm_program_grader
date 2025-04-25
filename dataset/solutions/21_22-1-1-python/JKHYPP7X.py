def modexp2(x,N):
    if x == 0:
        return 1;
    elif x % 2 == 0:
        teilErgebnis = modexp2(x//2,N);
        return (teilErgebnis*teilErgebnis % N);
    else:
        teilErgebnis = modexp2((x-1)//2,N);
        return (2*teilErgebnis*teilErgebnis % N);
    
def calc(n):
    return modexp2(n,1000000007)-1;