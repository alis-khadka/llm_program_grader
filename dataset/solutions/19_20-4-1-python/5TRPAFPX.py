# Node in parameter represents root of tree
def insert(root, insertNode):
    if root is None and insertNode is None:
        return None
    elif root is None:
        return insertNode
    elif insertNode is None:
        return root

    if root.key > insertNode.key:
        if root.left is None:
            root.left = insertNode
            insertNode.parent = root
        else:
            insert(root.left, insertNode)
    else:
        if root.right is None:
            root.right = insertNode
            insertNode.parent = root
        else:
            insert(root.right, insertNode)
    return root