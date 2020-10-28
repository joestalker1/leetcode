class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def largest_bst_subtree(root):
    max_size = 0
    max_root = None

    def helper(root):
        # Returns a tuple of (size, min_key, max_key) of the subtree.
        nonlocal max_size
        nonlocal max_root
        if root is None:
            # return inf as min key, - inf as max key, so it allows to any key be min/max these keys.
            return (0, float('inf'), float('-inf'))
        left = helper(root.left)
        right = helper(root.right)
        # left[2] is max key of left subtree, right[1] is min key of right subtree.
        if left[2] < root.key < right[1]:
            # if current key is root of proper BST
            size = left[0] + right[0] + 1
            # calculate size
            if size > max_size:
                max_size = size
                max_root = root
            # return size,min(current, and min of left subtree, and max current key and max subtree)
            return size, min(root.key, left[1]), max(root.key, right[2])
        else:
            # otherwise return size,min key is -inf, max key is +inf
            return 0, float('-inf'), float('inf')

    helper(root)
    return max_root


root = TreeNode(30)
root.left = TreeNode(10)
root.right = TreeNode(50)
print(largest_bst_subtree(root).key)