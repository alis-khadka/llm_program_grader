# Node in parameter represents root of tree
def delete(root, delete):
    if delete.left == None or delete.right == None:
        y = delete
    else:
        y = t_min(delete.right)
    if y.left != None:
        x = y.left
    else: x = y.right
    if x!= None:
        x.parent = y.parent
    if y.parent == None:
        root = x
    else:
        if y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
    if y != delete:
        delete.key = y.key
    return root
    
def t_min(node):
    while node.left !=None:
        node = node.left
    return node