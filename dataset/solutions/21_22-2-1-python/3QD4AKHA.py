def calc(A,B):
    dict = {}
    for i in range(0,len(A)):
        try: 
            dict[A[i]] = dict[A[i]] + 1
        except KeyError:
            dict[A[i]] = 1
    returnString = ""
    for i in range(0,len(B)):
        try:
            if dict[i]<=B[i]:
                returnString = returnString + "1"
            else:
                returnString = returnString + "0"
        except KeyError:
            returnString = returnString + "1"
    return returnString