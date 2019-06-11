# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        if not root:
            return True

        def traverse(node, last):
            if not node:
                return True
            left = traverse(node.left, last)
            if not left:
                return left
            if len(last) > 0 and last[0] > node.val:
                return False
            if len(last) == 0:
                last.append(node.val)
            else:
                last[0] = node.val
            return traverse(node.right, last)
        return traverse(root, [])




