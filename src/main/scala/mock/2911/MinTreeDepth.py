# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left_depth = float('inf')
            if node.left:
                left_depth = dfs(node.left)
            right_depth = float('inf')
            if node.right:
                right_depth = dfs(node.right)
            return 1 + min(left_depth, right_depth)

        return dfs(root)


