class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def compare(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return (s.val == t.val) and self.compare(s.left, t.left) and self.compare(s.right, t.right)

    def isSubtree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return (s.val == t.val and self.compare(s, t)) or self.compare(s.left, t) or self.compare(s.right, t)

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
print(sol.isSubtree(root, TreeNode(1)))