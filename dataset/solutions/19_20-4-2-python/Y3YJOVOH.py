# Node in parameter represents root of tree
def TREE_MINIMUM(root):
    x = root
    while(x.left != None):
        x = x.left
    return (x)


def delete(root, delete):
    y = Node
    x = Node
    if (delete.left == None or \
    delete.right == None):
        y = delete
    else:
        y = TREE_MINIMUM (delete.right)
    if (y.left != None):
        x = y.left
    else:
        x = y.right
    if (x != None):
        x.parent = y.parent
    if (y.parent == None):
        root = x
    else:
        if (y == y.parent.left):
            y.parent.left = x
        else:
            y.parent.right = x
    if (y != delete):
        delete.key = y.key
    y = None
    return (root)