# Node in parameter represents root of tree
def insert(root, insert):
	current_node = root
	last_node = None

	while current_node != None:
		last_node = current_node
		if insert.key < current_node.key:
			current_node = current_node.left
		else:
			current_node = current_node.right

	insert.parent = last_node

	if last_node == None:
		root = insert
	elif insert.key < last_node.key:
		last_node.left = insert
	else:
		last_node.right = insert
	return root