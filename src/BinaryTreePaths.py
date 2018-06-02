class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        l1 = [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)]
        l2 = [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]
        return l1 + l2


sol = Solution()
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# print(sol.binaryTreePaths(root))
# print(sol.binaryTreePaths(TreeNode(1)))
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
root.right = TreeNode(3)
print(sol.rootToLeafPaths(root))
