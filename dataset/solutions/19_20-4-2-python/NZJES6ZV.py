def tree_minimun(node):
    while node.left is not None:
        node = node.left

    return node

# Node in parameter represents root of tree
def delete(root, target):
    if root is target:
        return None

    current_node = root
    while current_node is not None and current_node.key != target.key:
        if target.key < current_node.key:
            current_node = current_node.left
        else:
            current_node = current_node.right

    if not current_node:
        return root

    if not current_node.left and not current_node.right:
        if current_node is current_node.parent.left:
            current_node.parent.left = None
        else:
            current_node.parent.right = None

    elif current_node.left and not current_node.right:
        if current_node is current_node.parent.left:
            current_node.parent.left = current_node.left
            current_node.left.parent = current_node.parent
        else:
            current_node.parent.right = current_node.left
            current_node.left.parent = current_node.parent

    elif current_node.right and not current_node.left:
        if current_node is current_node.parent.left:
            current_node.parent.left = current_node.right
            current_node.right.parent = current_node.parent
        else:
            current_node.parent.right = current_node.right
            current_node.right.parent = current_node.parent

    else:
        # successor = tree_successor(current_node)
        y = tree_minimun(current_node.right)
        if y.left is not None:
            x = y.left
        else:
            x = y.right

        if x is not None:
            x.parent = y.parent

        if y.parent is not None:
            if y is y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x

        if y is not current_node:
            current_node.key = y.key

    return root