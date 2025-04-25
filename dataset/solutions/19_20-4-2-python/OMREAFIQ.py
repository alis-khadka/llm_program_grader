def tree_minimum(node):
    while node.left != None: node = node.left
    return node

# Node in parameter represents root of tree
def tree_delete_node(root, delete):
    y = None # der (nach Tausch) zu löschende Knoten
    if delete.left == None or delete.right == None: y = delete
    else: y = tree_minimum(delete.right)
    x = None # Kind von y, das nicht None ist
    if y.left != None: x = y.left
    else: x = y.right
    # entferne y aus der Baumstruktur
    if x != None: x.parent = y.parent
    if y.parent == None: root = x
    elif y == y.parent.left: y.parent.left = x
    else: y.parent.right = x
    # kopiere Daten von y nach z
    if y != delete: delete.key = y.key
    
    return root

def search(node, k):
    while node != None and k != node.key:
        if k < node.key: node = node.left
        else: node = node.right
    return node

def delete(root, delete):
    return tree_delete_node(root, delete)

def inorder_tree_walk(x):
    if x != None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)