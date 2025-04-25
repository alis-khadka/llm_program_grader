# Node in parameter represents root of tree
def insert(root, insert):
    x = root
    y = None
    while x:
        y = x
        if insert.key < x.key:
            x = x.left
        else:
            x = x.right
    insert.parent = y
    if not y:
        root = insert
    elif insert.key < y.key:
        y.left = insert
    else:
        y.right = insert
    return root