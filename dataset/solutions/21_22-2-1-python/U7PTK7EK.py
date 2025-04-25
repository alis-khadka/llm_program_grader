def calc(A, B):
    
    counting_dict = {}
    for a_i in A:
        if a_i in counting_dict:
            counting_dict[a_i] += 1
        else:
            counting_dict[a_i] = 1

    s = ""
    for i in range(len(B)):
        if i in counting_dict:
            if counting_dict[i] <= B[i]:
                s = s + "1"
            else:
                s = s + "0"
        else:
            s = s + "1"
    return s