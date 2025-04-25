def calc(n):
    if(n==0):
        return 0
    return(dashier(n)-1) % 1000000007
    
def dashier(n):
    if (n==1):
        return(2)
    if (n%2==1):
        var=dashier(n-1) % 1000000007
        return(var*2) % 1000000007
    else:
        var=dashier(n/2) % 1000000007
        return(var*var) % 1000000007