def testN(f,a,b):

    c = (a+b)//2;
    if f(c-1) == 0 and f(c) == 1:
        return c;
    elif f(c) == 0 and f(c) == 0:
        return testN(f,c,b);
    else:
        return testN(f,a,c);

def calc(f):
    return testN(f,0,10**(18));