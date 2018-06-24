class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.closest = 0
        self.diff = float("inf")

    def closestValue(self, root, target):
        if not root:
            return self.closest
        diff = abs(root.val - target)
        if self.diff > diff:
            self.closest = root.val
            self.diff = diff
        self.closestValue(root.left, target)
        self.closestValue(root.right, target)
        return self.closest

