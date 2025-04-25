# Node in parameter represents root of tree
def delete(root, delete):
    if (not delete.left) or (not delete.right):
        y = delete
    else:
        y = TREEMINIMUM(delete.right)
    
    if y.left:
        x = y.left
    else:
        x = y.right
    
    if x:
        x.parent = y.parent
    
    if not y.parent:
        root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    
    if y != delete:
        delete.key = y.key
    
    return root
    
def TREEMINIMUM(x):
    while x.left:
        x = x.left
    return x