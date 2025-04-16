class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.data})"


# Pre-order traversal
def pre_order(node):
    if not node:
        return []
    lst = []
    lst.append(node.data)
    if node.left:
        lst += pre_order(node.left)
    if node.right:
        lst += pre_order(node.right)

    return lst


# In-order traversal
def in_order(node):
    if not node:
        return []
    lst = []
    if node.left:
        lst += in_order(node.left)
    lst.append(node.data)
    if node.right:
        lst += in_order(node.right)

    return lst


# Post-order traversal
def post_order(node):
    if not node:
        return []
    lst = []
    if node.left:
        lst += post_order(node.left)
    if node.right:
        lst += post_order(node.right)
    lst.append(node.data)

    return lst
