class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        self.succ = None
        def traverse(node):
            if not node:
                return
            if node.val > p and (not self.succ or self.succ > node.val):
                self.succ = node.val
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.succ


sol = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
print(sol.inorderSuccessor(root, 1))
