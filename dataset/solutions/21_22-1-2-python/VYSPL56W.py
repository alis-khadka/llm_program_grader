def calc(f):
    ran = range(10**18 + 1)
    while len(ran) > 10:
        #print("Guess: ", ran[len(ran)//2])
        if not f_N(ran[len(ran)//2]):
            #wenn guess < N
            ran = ran[len(ran)//2:]
        else:
            #wenn guess >= N
            ran = ran[0:len(ran)//2]
        #print(ran)
        #print("---------------------------------")
    for i in ran:
        #print("testing", i)
        if f_N(i):
            return i
    return ran[len(ran)-1]+1