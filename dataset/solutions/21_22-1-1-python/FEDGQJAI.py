def calc(a):
    if (a == 0):
        return 0
    return help(a)-1

def help(a):
    if (a == 0) :
        return 1

    recursive = help((a//2) % 1000000007)
    if (a % 2 == 0):
        return (recursive * recursive) % 1000000007
    return ((recursive*recursive)*2)% 1000000007