# Node in parameter represents root of tree
def insert(root, insert):
    curr = root
    prev = None
    
    while curr is not None:
        prev = curr
        if curr.key > insert.key:
            curr = curr.left
        elif curr.key < insert.key:
            curr = curr.right

    insert.parent = prev
    if prev is None:
        root = insert
    elif insert.key < prev.key:
        prev.left = insert
    elif insert.key > prev.key:
        prev.right = insert
    return root