def treeMinimum(x):
    while x.left is not None:
        x = x.left
    return x    

def treeSuccessor(x):
    if x.right is not None:
        return treeMinimum(x.right)
    else:
        y = x.parent
        while y is not None and x is y.right:
            x = y
            y = y.parent

        return y

# Node in parameter represents root of tree
def delete(root, delete):
    #Case 0 - Delete root while only root is in tree
    if root is delete and root.left is None and root.right is None:
        return None

    #Case 1 - Node is leaf
    if delete.left is None and delete.right is None:
        if delete.parent.left is delete:
            delete.parent.left = None
        else:
            delete.parent.right = None

    #Case 2 - Node has one successor
    elif (delete.left is None) ^ (delete.right is None):
        if delete.left is None:
            successor = delete.right
        else: 
            successor = delete.left

        if delete.parent.left is delete:
            delete.parent.left = successor
        else:
            delete.parent.right = successor

        successor.parent = delete.parent

    #Case 3 - Node has two successors
    else:
        #print("Case 3")
        successor = treeSuccessor(delete)

        if delete.right is not successor:
            successor.right = delete.right
            successor.right.parent = successor
        else:
            successor.right = None
            
        if successor.left is not successor:
            successor.left = delete.left
            successor.left.parent = successor
        else:
            successor.left = None
        
        if delete.parent.left is delete:
            delete.parent.left = successor
        else:
            delete.parent.right = successor

        if successor.parent is not delete:
            if successor.parent.right is successor:
                successor.parent.right = None
            elif successor.parent.left is successor:
                successor.parent.left = None
        
        successor.parent = delete.parent
    
    return root