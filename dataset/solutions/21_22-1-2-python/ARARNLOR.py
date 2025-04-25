def calc(f):
    upperLimit = 10**18
    lowerLimit = 0
    return findN(f, upperLimit, lowerLimit)
    
def findN(f, upper, lower):
    guess = (upper + lower) // 2
    if upper - lower == 1:
        # result equals upper
        return upper
    elif (f(guess) == 1):
        # geratene zahl ist größer gleich N
        upper = guess
        return findN(f, upper, lower)
    else:
        # geratene zahl ist echt kleiner als N
        lower = guess
        return findN(f, upper, lower)