# Node in parameter represents root of tree
def delete(root, delete):
    # wenn einen oder keinen Nachfolger
    if delete.left == None or delete.right == None:
        y = delete
    # wenn zwei Nachfolger, dann kleinsten von den Großen
    else: 
        y = delete.right
        while (y.left): y = y.left
    # wenn es Nachfolger gibt dann left oder right/None
    if y.left:
        x = y.left
    else:
        x = y.right
        
    # Der Nachfolger von delete bekommt neuen parent
    if (x): x.parent = y.parent
    # wenn delete die Wurzel war, also parent = None
    if (not y.parent): root = None
    # wenn nicht Wurzel, dann den neuen parent anbinden
    else:
        if y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        y.parent = None
    if (y is not delete):
        delete.key = y.key
    
    return root