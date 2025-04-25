def tree_min(node):
    while node.left is not None:
        node = node.left
    return node


def successor(node):
    if node.right is not None:
        return tree_min(node.right)
    else:
        y = node.parent
        while y is not None and Node == y.right:
            x = y
            y = y.parent
        return y


def transplant(root, node1, node2):
    if node1.parent is None:
        root = node2
    elif node1 == node1.parent.left:
        node1.parent.left = node2
    else:
        node1.parent.right = node2
    if node2 is not None:
        node2.parent = node1.parent

    return root


# Node in parameter represents root of tree
def delete(root, delete):
    # Case 1: delete has no left child. Replace with right child
    # which might be None
    if delete.left is None:
        root = transplant(root, delete, delete.right)

    # Case 2: delete has a left child, but no right child
    elif delete.right is None:
        root = transplant(root, delete, delete.left)

    # Case 3: delete has two children
    else:
        succ = successor(delete)
        if succ.parent != delete:
            root = transplant(root, succ, succ.right)
            succ.right = delete.right
            succ.right.parent = succ
        root = transplant(root, delete, succ)
        succ.left = delete.left
        succ.left.parent = succ

    return root