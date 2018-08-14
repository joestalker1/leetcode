class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if not root.left or not root.right:
            return 1 + max(left_depth, right_depth)
        return 1 + min(left_depth, right_depth)

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
print(sol.minDepth(root))