# Node in parameter represents root of tree
def delete(root, deleteNode):
    # Sonderfall: None
    if (root is None) or (deleteNode is None):
        return root

    # Fall 1: deleteNode hat keine Kinder.
    if (deleteNode.left is None) and (deleteNode.right is None):
        newNode = None
        # Sonderfall: Einelementiger Baum
        if deleteNode is root:
            return None

    # Fall 2: deleteNode hat ein Kind.
    elif deleteNode.left is None:
        newNode = deleteNode.right
    elif deleteNode.right is None:
        newNode = deleteNode.left

    # Fall 3: delteNode hat 2 Kinder.
    else:
        # Finde das kleinste Element des linken Teilbaums von deleteNode und mache es zum newNode.
        newNode = treeMinimum(deleteNode.right)
        # Falls newNode das direkte Kind von deleteNode ist, ist er bereits mit dem korrekten rechten Teilbaum verbunden.
        # Ansonsten:
        if newNode is not deleteNode.right:
            # Entferne newNode von seiner alten Position im Baum.
            if newNode.right is None:
                if newNode is newNode.parent.left:
                    newNode.parent.left = None
                else:
                    newNode.parent.right = None
            else:
                newNode.right.parent = newNode.parent
                if newNode is newNode.parent.left:
                    newNode.parent.left = newNode.right
                else:
                    newNode.parent.right = newNode.right
            # Hänge deleteNodes rechten Teilbaum an newNode
            deleteNode.right.parent = newNode
            newNode.right = deleteNode.right
        # Hänge deleteNodes linken Teilbaum an newNode
        deleteNode.left.parent = newNode
        newNode.left = deleteNode.left

    # Entferne deleteNode von seinem Parent und verbinde stattdessen newNode.
    if deleteNode.parent is not None:
        if deleteNode is deleteNode.parent.left:
            deleteNode.parent.left = newNode
        else:
            deleteNode.parent.right = newNode

    # Verbinde newNode mit seinem neuen Parent Teil 2.
    if newNode is not None:
        newNode.parent = deleteNode.parent
        if deleteNode is root:
            root = newNode

    return root

def treeMinimum(root):
    if root is None:
        return None

    if root.left is None:
        return root
    else:
        return treeMinimum(root.left)