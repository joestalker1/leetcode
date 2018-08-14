class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


sol = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
print(sol.lowestCommonAncestor(root, root, root.left))
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
print(sol.lowestCommonAncestor(root, 2, 4))



