giftNum = []


def calc(A, B):
    output = []
    giftNum = B.copy()

    for i in range(0, len(giftNum)): # max O(n)
        giftNum[i] = 0
    for i in range(0, len(A)):
        giftNum[A[i]] += 1
    for i in range(0, len(B)):      # max: O(n)
        if giftNum[i] <= B[i]:
            output.append(1)
        else:
            output.append(0)

    listToStr = ''.join(map(str, output))   # max: O(n)
    return listToStr