class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        self.max_freq = 0

    def count_freq(self, root, a):
        if not root:
            return 0
        if root.val > a:
            return self.count_freq(root.left, a)
        if root.val < a:
            return self.count_freq(root.right, a)
        if root.val == a:
            return 1 + self.count_freq(root.left, a) + self.count_freq(root.right, a)

    def findMode(self, root):
        if not root:
            return self.res
        freq = self.count_freq(root, root.val)
        if freq > self.max_freq:
            self.max_freq = freq
            self.res = [root.val]
        elif freq == self.max_freq:
            self.res.append(root.val)
        self.findMode(root.left)
        self.findMode(root.right)
        return self.res

sol = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
print(sol.findMode(root))
