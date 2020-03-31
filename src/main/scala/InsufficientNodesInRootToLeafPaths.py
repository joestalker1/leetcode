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
                return sum_so_far >= limit
            new_sum = node.val + sum_so_far
            left_subtree = dfs(node.left, new_sum)
            right_subtree = dfs(node.right, new_sum)
            if not left_subtree:
                node.left = None
            if not right_subtree:
                node.right = None
            if not left_subtree and not right_subtree and node.left and node.right or not left_subtree and not node.right or not right_subtree and not node.left:
                return False
            return True

        if not dfs(root, 0):
            root = None
        return root
