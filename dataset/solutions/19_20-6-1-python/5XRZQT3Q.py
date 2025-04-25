def editDistance(a, b):
    if len(a) > len(b):
        a, b = b, a

    total = range(len(a) + 1)
    for i_b, s_b in enumerate(b):
        tmpdist = [i_b+1]
        for i_a, s_a in enumerate(a):
            if s_a == s_b:
                tmpdist.append(total[i_a])
            else:
                tmpdist.append(1 + min((total[i_a], total[i_a + 1], tmpdist[-1])))
        total = tmpdist
    return total[-1]