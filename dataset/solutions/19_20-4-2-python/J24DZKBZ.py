# Node in parameter represents root of tree
def wholeTree(root):
    if root is not None:
        wholeTree(root.left)
        wholeTree(root.right)
        return root
    
def minTree(node):
    while node.left is not None:
        node = node.left
    return node

def delete(root, delete):
    x = None
    if delete.right is None or delete.left is None: #Fall 1 und 2
        y = delete
    else: y = minTree(delete.right)
    if y.left is not None: x = y.left
    else: x = y.right
    
    if x is not None: x.parent = y.parent
    if y.parent is None: root = x
    else:
        if y == y.parent.left: y.parent.left = x
        else: y.parent.right = x
    if y is not delete: delete.key = y.key
    y = x
    return (wholeTree(root))