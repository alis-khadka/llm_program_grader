def Calculator(inputarray, stack):
    """Berechnet das Ergebnis des Inputs.

    Parameters
    ----------
    inputarray : list of str
        Input im Format: ["1", "2", "*", "3", "4", "*", "+"])
    stack : Stack object

    Returns
    -------
    result : int
        Das Ergebnis der Berechnung.
    """

    for item in inputarray:
        if item == "+":
            x = int(stack.pop())
            y = int(stack.pop())
            stack.push(y + x)
        elif item == "-":
            x = int(stack.pop())
            y = int(stack.pop())
            stack.push(y - x)
        elif item == "*":
            x = int(stack.pop())
            y = int(stack.pop())
            stack.push(y * x)
        elif item == "/":
            x = int(stack.pop())
            y = int(stack.pop())
            stack.push(y / x)
        else:
            stack.push(item)

    return stack.head()