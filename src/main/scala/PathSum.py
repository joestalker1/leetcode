class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def is_leaf(self, root):
        return root and not root.right and not root.left

    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if sum == 0 and self.is_leaf(root):
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

