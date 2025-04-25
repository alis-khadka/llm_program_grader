W = [9,1,2,8,3,4,7,6,5]

def opt(W):
    a = 0
    b = 0
    x = 0
    z = 0

    for i in range(len(W)):
        if(i%2 ==0):
            a += W[i]
            z=1
        else:
            b += W[i]
            z=0
        if( a >= b and z == 0):
            x += a
            a=0
            b=0

        if( b >= a and z==1):
            x += b
            a=0
            b=0

    x += max(a,b)

    return x