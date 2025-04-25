def delete(root, delete):
    if delete.left == None or delete.right == None:
        b = delete
    else: 
        b = delete.right
        while b.left: b = b.left
    if b.left:
        a = b.left
    else:
        a = b.right
    if a: a.parent = b.parent
    if not b.parent: root = None
    else:
        if b == b.parent.left:
            b.parent.left = a
        else:
            b.parent.right = a
        b.parent = None
    if b is not delete:
        delete.key = b.key
    return root