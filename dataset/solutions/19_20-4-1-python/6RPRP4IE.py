# Node in parameter represents root of tree
def insert(root, insert):
    par = None
    x = root
    while(x != None):
        par = x
        if(insert.key < x.key):
            x=x.left
        else:
            x=x.right
    insert.parent = par
    if(par==None):
        root = insert
    elif(insert.key  < par.key):
        par.left = insert
    else:
        par.right = insert
    return root