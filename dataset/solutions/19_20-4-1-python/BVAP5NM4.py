# Node in parameter represents root of tree
def treewalk(root):
    if root is not None:
        treewalk(root.left)
        treewalk(root.right)
        return root


def insert(root, insert):
    x = root
    y = None
    while x is not None:
        y = x
        if insert.key < y.key:
            x = x.left
        else:
            x = x.right
    insert.parent = y
    if y is None:
        root = insert
    elif insert.key < y.key:
        y.left = insert
    else:
        y.right = insert

    return treewalk(root)