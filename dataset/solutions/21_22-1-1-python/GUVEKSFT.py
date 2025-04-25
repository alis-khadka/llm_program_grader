def calc(b):
    if b == 0: return 0
    return (twopowb(b) - 1) % 1000000007


def twopowb(b):
    if b == 1: return 2
    if b % 2 == 0: # gerade
        val = twopowb(b // 2)
        return (val * val )% 1000000007
    else: #b ungerade
        return (twopowb(b - 1) * 2)% 1000000007