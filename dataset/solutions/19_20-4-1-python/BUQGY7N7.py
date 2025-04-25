# Node in parameter represents root of tree
def insert(root, insert):
    currentNode = root
    currentParent = None

    while currentNode is not None:
        currentParent = currentNode
        if(insert.key < currentNode.key):
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right

    insert.parent = currentParent

    if currentParent is None:
        root = insert
    elif insert.key < currentParent.key:
        currentParent.left = insert
    else:
        currentParent.right = insert

    return root