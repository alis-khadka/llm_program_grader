# Node in parameter represents root of tree
def delete(root, delete):
    if delete.left == None or delete.right == None: delete_node = delete
    else: delete_node = TREE_SUCCESSOR(delete.right)
    if delete_node.left != None: not_nil_child = delete_node.left
    else: not_nil_child = delete_node.right
    if not_nil_child != None: not_nil_child.parent = delete_node.parent
    if delete_node.parent == None: root = not_nil_child
    else:
        if delete_node == delete_node.parent.left: delete_node.parent.left = not_nil_child
        else: delete_node.parent.right = not_nil_child
    if delete_node != delete: delete.key = delete_node.key
    return root

def TREE_SUCCESSOR(node):
    while node.left != None: node = node.left
    return node