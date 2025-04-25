# Node in parameter represents root of tree
def insert(root, new):
    if root == None:
        return new
    if root.key > new.key:
        if root.left == None:
            root.left = new
            new.parent = root
        else:
            insert(root.left, new)
    else:
        if root.right == None:
            root.right = new
            new.parent = root
        else:
            insert(root.right, new)
    return root