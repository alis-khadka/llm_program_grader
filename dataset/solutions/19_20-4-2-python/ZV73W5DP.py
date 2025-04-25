# Node in parameter represents root of tree
def delete(root, delnode):
    if delnode is None:
        return root
    if delnode == root and root.left == root.right and root.left is None:
        return None
    if delnode.left is None:
        transplant(delnode, delnode.right)
    elif delnode.right is None:
        transplant(delnode, delnode.left)
    else:
        nodey = delnode.right
        while nodey.left is not None:
            nodey = nodey.left
        if nodey.parent != delnode:
            transplant(nodey, nodey.right)
        transplant(delnode, nodey)
        nodey.left = delnode.left
        nodey.left.parent = nodey
        if nodey != delnode.right:
            nodey.right = delnode.right
            nodey.right.parent = nodey
        if delnode != root:
            nodey.parent = delnode.parent
        else:
            nodey.parent = None
    return root
    
def transplant(n1, n2):
    if n1.parent is None:
        n2.parent = None
    elif n1.parent.left is not None and n1.key == n1.parent.left.key:
        n1.parent.left = n2
    else:
        n1.parent.right = n2
    if n2 is not None:
        n2.parent = n1.parent