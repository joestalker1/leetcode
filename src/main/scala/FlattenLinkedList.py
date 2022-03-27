def merge(self, a, b):
    # if first linked list is empty then second
    # is the answer
    if (a == None):
        return b

    # if second linked list is empty then first
    # is the result
    if (b == None):
        return a

    # compare the data members of the two linked lists
    # and put the larger one in the result
    result = None

    if (a.data < b.data):
        result = a
        result.down = self.merge(a.down, b)
    else:
        result = b
        result.down = self.merge(a, b.down)

    result.right = None
    return result

def flatten(self, root):

    # Base Case
    if (root == None or root.right == None):
        return root
    # recur for list on right

    root.right = self.flatten(root.right)

    # now merge
    root = self.merge(root, root.right)

    # return the root
    # it will be in turn merged with its left
    return root
