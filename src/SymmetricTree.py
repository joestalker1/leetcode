class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def is_mirror(self, x, y):
        if not x and not y:
            return True
        if not x or not y:
            return False
        if x.val != y.val:
            return False
        return self.is_mirror(x.left, y.right) and self.is_mirror(x.right, y.left)

    def isSymmetric(self, root):
        if not root:
            return True
        return self.is_mirror(root, root)


sol = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.left.right = TreeNode(1)
root.left.right.left = TreeNode(2)
root.right =  TreeNode(1)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(2)
print(sol.isSymmetric(root))