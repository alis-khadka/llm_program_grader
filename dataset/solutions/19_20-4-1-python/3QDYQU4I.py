# Node in parameter represents root of tree
def insert(root, target):
    if root is None:
        return target
    # start traversing at the root to find the place to append insert
    x = root
    while True:
        # choose left or right subtree to insert
        # if the chosen subtree is empty, insert there
        if target.key < x.key:
            if x.left is not None:
                x = x.left
            else:
                x.left = target
                target.parent = x
                break
        else:
            if x.right is not None:
                x = x.right
            else:
                x.right = target
                target.parent = x
                break
    return root