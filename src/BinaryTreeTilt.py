class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def find_tilt_and_sum(self, root, res):
        if not root:
            return 0
        left = self.find_tilt_and_sum(root.left, res)
        right = self.find_tilt_and_sum(root.right, res)
        res.append(abs(left - right))
        return root.val + left + right

    def findTilt(self, root):
        res = []
        left_sum = self.find_tilt_and_sum(root.left, res) if root.left else 0
        right_sum = self.find_tilt_and_sum(root.right, res) if root.right else 0
        res.append(abs(left_sum - right_sum))
        tilt = 0
        for r in res:
            tilt += r
        return tilt

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
#print(sol.findTilt(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
print(sol.findTilt(root))