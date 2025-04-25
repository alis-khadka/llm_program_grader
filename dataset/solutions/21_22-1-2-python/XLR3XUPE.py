MITTE = int(1e18 // 2)


def calc(f):
    result = MITTE

    result = realrecursion(f, MITTE, MITTE)

    return result


def realrecursion(f, result, jump):

    if f(result) and not f(result - 1):
        return result

    if jump != 1:
        jump = int(jump // 2)

    if f(result):
        result -= jump
        return realrecursion(f, result, jump)
    else:
        result += jump
        return realrecursion(f, result, jump)