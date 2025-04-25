# Node in parameter represents root of tree
def insert(root, target):
    if not root:
        return target

    if target.key < root.key:
        if root.left:
            insert(root.left, target)
        else:
            root.left = target
            root.left.parent = root
    
    elif target.key >= root.key:
        if root.right:
            insert(root.right, target)
        else:
            root.right = target
            root.right.parent = root
        
        
    return root