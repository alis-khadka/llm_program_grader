class Node:
    def __init__(self):
        self.parent = None
        self.key = None
        self.left = None
        self.right = None

class GoodNode:
    def __init__(self, key, left = None, right = None):
        self.parent = None
        self.key = key
        self.children = {'left': left, 'right': right}
        if left is not None:
            self.children['left'].parent = self
        if right is not None:
            self.children['right'].parent = self
                    
def kind(self):
    if self.parent is None:
        return None
    else:
        if self.parent.children['left'] is self:
            return 'left'
        elif self.parent.children['right'] is self:
            return 'right'
        else:
            raise Exception("illformed node: i'm not my parent's child :(")

def left(self):
    return self.children['left']

def right(self):
    return self.children['right']

def minimum(self):
    result = self
    while result.children['left'] is not None:
        result = result.children['left']
    return result

def children_count(self):
    c = 0
    if self.children['left'] is not None:
        c+= 1
    if self.children['right'] is not None:
        c+= 1
    return c

def first_nonnull_child(self):
    if self.children['left'] is not None:
        return self.children['left']
    elif self.children['right'] is not None:
        return self.children['right']
    else:
        return None

# remove key that belongs to this node from its tree
# this might involve removing the entire node from its tree
# return new root
def remove_key(self, root):
    if children_count(self) == 2:
        # remove minimum after this node and put it in place of self
        right_minimum = minimum(right(self))
        minimum_key = right_minimum.key
        root = remove_key(right_minimum, root)
        assert root is not None
        self.key = minimum_key
        return root
    elif children_count(self) == 1:
        # become your child
        child = first_nonnull_child(self)
        self.key = child.key
        root = remove_key(child, root)
        assert root is not None
        return root
    else:
        selfkind = kind(self)
        # detach from parent
        parent = self.parent
        self.parent = None
        if parent is not None:
            parent.children[selfkind] = None
            return root
        else:
            return None

def compare(self, other):
    assert self is not None
    if other is None:
        return False
    if self.key != other.key:
        return False
    for kind in ['right', 'left']:
        if self.children[kind] is not None:
            if compare(self.children[kind], other.children[kind]) == False:
                return False
        elif other.children[kind] is not None:
            return False
    return True

def fuckoff(uhh_node):
    if uhh_node is None:
        return 
    uhh_node.children = {'left': uhh_node.left, 'right': uhh_node.right}
    del uhh_node.left
    del uhh_node.right
    fuckoff(uhh_node.children['left'])
    fuckoff(uhh_node.children['right'])

def fuckon(self):
    if self is None:
        return
    self.left = self.children['left']
    self.right = self.children['right']
    del self.children
    fuckon(self.left)
    fuckon(self.right)
        

# Node in parameter represents root of tree
def delete(root, to_remove):
    fuckoff(root)
    root = remove_key(to_remove, root)
    fuckon(root)
    return root