def add(x,y):
    return x+y
def minus(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return int(x/y)

def Calculator(inputarray, stack):
    #lst = []
    for elem in inputarray:
        if elem   == "+":
            y = stack.pop()
            x = stack.pop()
            stack.push(add(x,y))
        elif elem == "-":
            #print(type(stack))
            y = stack.pop()
            x = stack.pop()
            stack.push(minus(x,y))
        elif elem == "*":
            y = stack.pop()
            x = stack.pop()
            stack.push(mult(x,y))
        elif elem == "/": 
            y = stack.pop()
            x = stack.pop()
            stack.push(div(x,y))
        else:
            stack.push(int(elem))
    return stack.head()