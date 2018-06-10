class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        left_res = self.isSameTree(p.left, q.left)
        right_res = self.isSameTree(p.right, q.right)
        return left_res and right_res

