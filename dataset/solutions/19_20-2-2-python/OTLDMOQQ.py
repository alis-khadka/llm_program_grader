def Calculator(inputarray, stack):
    while len(inputarray)>0:
        ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y),
            "*": (lambda x,y: x*y), "/": (lambda x,y: int(x/y))}
        n = inputarray.pop(0)
        if n not in ops:
            stack.push(int(n))
        else:
            y = stack.pop()
            x = stack.pop()
            stack.push(ops[n](x,y))
    return stack.pop()