class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        if not t1 and not t2:
            return None
        if not t1:
            return t2
        if not t2:
            return t1
        val = t1.val + t2.val
        new_node = TreeNode(val)
        new_node.left = self.mergeTrees(t1.left, t2.left)
        new_node.right = self.mergeTrees(t1.right, t2.right)
        return new_node
