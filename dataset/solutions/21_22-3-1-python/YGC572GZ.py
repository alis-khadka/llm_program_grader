def opt(W):
    on = 0
    off = 0
    for i in W:
        pon = on
        on = off + i
        off = max(pon,off)
    return max(on,off)