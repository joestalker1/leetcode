# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.right) + self.countNodes(root.left)

sol = Solution()
#print(sol.countNodes(TreeNode(1)))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print(sol.countNodes(root))