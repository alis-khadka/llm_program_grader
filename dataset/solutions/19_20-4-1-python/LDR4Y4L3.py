def insert(root, target):
    
    
    if root == None: 
        root = Node()
        root.key = target.key
        return root
    
    #rechts rum
    if target.key > root.key:
        #akt Wert == None
        if root.right == None:     
            root.right = target
            target.parent = root
        else:
            insert(root.right, target)
            
    #links rum     
    else: 
        if root.left == None:   
            root.left = target
            target.parent = root
        else:
            insert(root.left, target)
            
    return root