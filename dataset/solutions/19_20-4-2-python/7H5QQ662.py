# Node in parameter represents root of tree
def delete(root, node):
    if root is None or node is None:
        return None
    if root is node:
        return None
    if not node.left:
        transplant(node, node.right)
    elif not node.right:
        transplant(node, node.left)
    else:
        # 2 Kinder
        y = tree_minimum(node.right)
        if y is not node.right:
            transplant(y, y.right)
            y.right = node.right
            y.right.parent = y
        transplant(node, y)
        y.left = node.left
        y.left.parent = y
    return root

# Ersetzt alten Knoten mit neuem Knoten
def transplant(old_node, new_node):
    if new_node:
        new_node.parent = old_node.parent
    if old_node.parent:
        if old_node.parent.left is old_node:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node

def tree_minimum(node):
    while node.left:
        node = node.left
    return node