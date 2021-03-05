class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def is_symmetric(left, right):
    # check value
    if left.val != right.val:
        return False
    #if children are available
    if not left.children and not right.children:
        return True
    #if children sizes are the same
    if len(left.children) != len(right.children):
        return False
    #compare the leftmost and rightmost children
    k = len(left.children)
    for i in range(k):
        if not is_symmetric(left.children[i], right.children[k - 1 - i]):
            return False

    return True


root = Node(0)
is_symmetric(root, root)
