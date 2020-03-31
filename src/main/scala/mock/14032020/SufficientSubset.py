# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sufficientSubset(self, root, limit):
        if not root:
            return root

        def dfs(node, sum_so_far):
            if not node:
                return True
            if not node.right and not node.left:
                if sum_so_far < limit:
                    return False
                return True
            if node.val + sum_so_far < limit:
                node.left = None
                node.right = None
                return False
            left_subtree = dfs(node.left, node.val + sum_so_far)
            right_subtree = dfs(node.right, node.val + sum_so_far)
            if not left_subtree:
                node.left = None
            if not right_subtree:
                node.right = None
            return left_subtree or right_subtree

        dfs(root, 0)
        return root


