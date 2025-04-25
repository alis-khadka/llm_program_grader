def opt(W):
    n = len(W)
    win = [[0,0] for _ in range(n)] 
    # Liste zum Speichern des max Gewinns bis einschl. W_i
    # an [0] bei nicht-Verwendung, an [1] bei Verwendung von W_i
    for i, w in enumerate(W):
        if i == 0:   # Fall w = erstes Element
            win[0][0], win[0][1] = 0, w
        elif i == 1:   #Fall w = zweites Element
            win[1][0], win[1][1] = win[0][1], w if w > W[i-1] else W[i-1]
        else:
            win[i][0] = max(win[i-1])
            win[i][1] = max(win[i-1][1], win[i-2][1]+w)
    return max(win[-1])