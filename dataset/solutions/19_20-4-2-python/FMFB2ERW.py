def treeoutput(root):
  if root != None:
    treeoutput(root.left)
    treeoutput(root.right)
  return root

def tree_minimum(inp):
    while inp.left != None:
        inp = inp.left
    return inp

# Node in parameter represents root of tree
def delete(root, delete):
    if delete.left == None or delete.right == None:
        y = delete
    else:
        y = tree_minimum(delete.right)
    if y.left != None:
        x = y.left
    else:
        x = y.right
    if x != None:
        x.parent = y.parent
    if y.parent == None:
        root = x
    else:
        if y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
    if y != delete:
        delete.key = y.key
    y = None
    return treeoutput(root)