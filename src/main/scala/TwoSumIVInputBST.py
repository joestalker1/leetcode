class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_sum(self, root, k, nums):
        if not root:
            return False
        if (k - root.val) in nums:
            return True
        nums.add(root.val)
        return self.find_sum(root.left, k, nums) or self.find_sum(root.right, k, nums)

    def findTarget(self, root, k):
        return self.find_sum(root, k, set())

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
print(sol.findTarget(root, 9))