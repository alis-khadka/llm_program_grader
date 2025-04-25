def treeminimum(node):
    while(node.left != None):
            node = node.left
    return node

# Node in parameter represents root of tree
def delete(root, delete):
    if(delete.left == None or delete.right == None):
        newdel = delete
    else:
        newdel = treeminimum(delete.right)
    if(newdel.left != None):
        newdelchild = newdel.left
    else:
        newdelchild = newdel.right
    if(newdelchild != None):
        newdelchild.parent = newdel.parent
    if(newdel.parent == None):
        root = newdelchild
    else:
        if(newdel == newdel.parent.left):
            newdel.parent.left = newdelchild
        else:
            newdel.parent.right = newdelchild
    if(newdel != delete):
        delete.key = newdel.key
    del newdel
        
    return root