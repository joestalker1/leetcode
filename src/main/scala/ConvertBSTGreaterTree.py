class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if not root:
            return None
        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)
        return root

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
root = sol.convertBST(root)
print(root)