# Node in parameter represents root of tree
def insert(root, target):
    before = None
    is_left_child = None
    current = root
    while current is not None:
        before = current
        if target.key >= current.key:
            is_left_child = False
            current = current.right
        else:
            is_left_child = True
            current = current.left
        
    if before != None:
        target.parent = before
        if is_left_child:
            before.left = target
        else:
            before.right = target
        return root
    else:
        return target