# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def smallestFromLeaf(self, root):
        if not root or len(root) == 1:
            return root

        def traverse(node):
            if not node:
                return None
            s1 = traverse(node.left)
            s2 = traverse(node.right)
            if not s1 or not s2:
                res = ''
            else:
                res = min(s1, s2)
            return res + node.val
        return traverse(root)

