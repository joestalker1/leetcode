from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        idx = 0

        def dfs(lower, upper):
            nonlocal idx
            if idx == len(preorder):
                return None
            val = preorder[idx]
            if val < lower or val > upper:
                return None
            node = TreeNode(val)
            node.left = dfs(lower, val)
            node.right = dfs(val, upper)
            return node

        idx = 0
        return dfs(-inf, inf)