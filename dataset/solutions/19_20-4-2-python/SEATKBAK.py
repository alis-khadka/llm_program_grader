# Node in parameter represents root of tree
def tree_minimum(node):
    while node.left is not None:
        node = node.left
    return node



def delete(root, delete):
    """
    case 1: delete has no child
        - node to delete is also delete
    case 2: delete has 1 child
        - node to delete is also delete
        - reconnect child of delete to parent of delete
    case 3: delete has 2 child
        - replace value of delete by value of delete_sucessor
        - node_to_delete is delete_sucessor
        - bind childrend and parent of delete_sucessor together
    """
    # choose node_to_delete depends on case
    if delete.right is None or delete.left is None:  # case 1 and 2
        node_to_delete = delete
    else:  # case 3
        node_to_delete = tree_minimum(delete.right)

    # choose child of node_to_delte depends on case
    if node_to_delete.left is not None:  # case 2 for left child
        child_node_to_delete = node_to_delete.left
    else:  # case 2 for right child and case 3
        child_node_to_delete = node_to_delete.right


    # bind child and parent depends (both in case 2 and 3 similar)
    if child_node_to_delete is not None:
        child_node_to_delete.parent = node_to_delete.parent
    
    if node_to_delete.parent is None:
        root = child_node_to_delete
    else:
        if node_to_delete == node_to_delete.parent.left:
            node_to_delete.parent.left = child_node_to_delete
        else:
            node_to_delete.parent.right = child_node_to_delete

    # for case 3: copy data form node_to_delete to delete
    if delete is not node_to_delete:
        delete.key = node_to_delete.key

    del node_to_delete

    if root is not None:
        return root
    else:
        return None