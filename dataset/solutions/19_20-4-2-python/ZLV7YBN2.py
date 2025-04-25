def treewalk(root):
    if root is not None:
        treewalk(root.left)
        treewalk(root.right)
        return root


def tree_min(node):
    while node.left is not None:
        node = node.left
    return node

# Node in parameter represents root of tree
def delete(root, z):
    if z.left is None or z.right is None:
        y = z
    else:
        y = tree_min(z.right)
    if y.left is not None:
        x = y.left
    else:
        x = y.right
    if x is not None:
        x.parent = y.parent
    if y.parent is None:
        root = x
    else:
        if y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
    if y != z:
        z.key = y.key
    y = None

    return treewalk(root)