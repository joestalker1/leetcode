# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from  collections import defaultdict

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        m = defaultdict(lambda :0)
        max_val = -float('inf')
        max_level = 0
        def traverse(node, level, m):
            nonlocal max_val, max_level
            if not node:
                return
            m[level] += node.val
            if max_val < m[level]:
                max_val = max(max_val, m[level])
                max_level = level
            traverse(node.left, level + 1, m)
            traverse(node.right, level + 1, m)

        traverse(root, 1, m)
        return max_level

