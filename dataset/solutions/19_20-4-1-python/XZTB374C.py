# Node in parameter represents root of tree
def insert(root, to_insert):
    if root is None:
        return to_insert
        
    if to_insert.key < root.key:
        root.left = insert(root.left, to_insert)
        root.left.parent = root
    else:
        root.right = insert(root.right, to_insert)
        root.right.parent = root
    return root