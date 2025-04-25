# Node in parameter represents root of tree
def insert(root, insert):
    y = None
    x = root
    while (x):
        y = x
        if x.key > insert.key:
             x = x.left
        else:
             x = x.right
    insert.parent = y
    if (not y):
         root = insert
    else:
         if y.key > insert.key:
             y.left = insert
         else:
             y.right = insert
    return root