class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sum_of_greater(self, root, a):
        if not root:
            return 0
        b = 0
        if root.left and root.left.val > a:
            b = self.sum_of_greater(root.left, a)
        if root.right and root.right.val > a:
            b += self.sum_of_greater(root.right, a)
        if root.val > a:
            b += root.val
        return b

    def create_bst(self, node, root):
        if not root or not node:
            return None
        a = self.sum_of_greater(root, node.val)
        new_node = TreeNode(node.val + a)
        new_node.left = self.create_bst(node.left, root)
        new_node.right = self.create_bst(node.right, root)
        return new_node

    def convertBST(self, root):
        return self.create_bst(root, root)

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
root = sol.convertBST(root)
print(root)