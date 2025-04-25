def calc(A,B):
    s = ""
    A_new = count_elements(A, B)
    for index, ele in enumerate(B):
        if ele >= A_new[index]:
            s+="1"
        else:
            s+="0"
    return s

def count_elements(A, B):
    A_new = [0] * (len(B)+1)

    for ele in A:
        A_new[ele]+=1
    return A_new