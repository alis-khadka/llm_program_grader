def minimum(x):  
# Aufruf mit TREE-MINIMUM(T.root) 
    while x.left != None :
        x = x.left 
    return x  


# Node in parameter represents root of tree
def delete(root, z):
    # y: der (nach Tausch) zu löschende Knoten 
    if z.left == None or z.right == None:
        y = z 
    else:
        y = minimum( z.right ) # Cormen: TR
    # x: Kind von y, das nicht NIL ist 
    if y.left != None:
        x = y.left 
    else:
        x = y.right 
    # entferne y aus der Baumstruktur 
    if x != None:
        x.parent = y.parent
    if y.parent == None:
        root = x 
    elif y == y.parent.left:
        y.parent.left = x 
    else:
        y.parent.right = x 
    # kopiere Daten von y nach z 
    if y != z:
        z.key = y.key 
    return root