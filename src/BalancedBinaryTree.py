class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.balanced = True

    def depth_of(self, root):
        if not root:
            return 0
        left = self.depth_of(root.left)
        right = self.depth_of(root.right)
        if abs(left - right) > 1:
            self.balanced = False
        return 1 + max(left, right)

    def isBalanced(self, root):
        self.depth_of(root)
        return self.balanced

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(4)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)
root.left.left.left.right = TreeNode(5)
root.left.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.left.left = TreeNode(4)
root.right.left.right = TreeNode(4)
root.right.right = TreeNode(3)
print(sol.isBalanced(root))