import re

def Calculator(inputarray, stack):
    for i in range(len(inputarray)):

        if inputarray[i] not in "/*+-":
            stack.push(inputarray[i])

        if inputarray[i] in "/*+-":
            last = stack.pop()
            first = stack.pop()
            if inputarray[i] == '/' and last == '0':
                return 'Error: division by 0'

            result = eval(str(first)+inputarray[i]+str(last))
            stack.push(str(int((result))))

    return result