# Node in parameter represents root of tree
def insert(x, z):
    if z == None:
        return x
    elif x == None:
        return z
    else:
        if z.key < x.key:
            if x.left != None:
                x.left = insert(x.left, z) 
            else:
                z.parent = x
                x.left = z 
        elif x.right != None:
            x.right = insert(x.right, z)
        else:
            z.parent = x 
            x.right = z 
        return x