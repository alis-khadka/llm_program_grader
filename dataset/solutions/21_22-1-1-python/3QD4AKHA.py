def calc(n):
    if  n > 1000000000:
         return -1
    if n==0 :
        return 0
    
    return ( potenz2(n)-1) 
   
def potenz2(n):
    if n==0:
        return 1
     
    if n%2==0:
        p = potenz2(n//2)
        return (p*p)%1000000007 
     
    if n%2== 1:
        p = potenz2((n-1)//2)
        return (2*p*p)%1000000007 
     
    return -1