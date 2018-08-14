class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sorted_array_to_bst(self, nums, lo, hi):
        if lo >= hi:
            return TreeNode(nums[lo])
        if (hi - lo) == 1:
            t1 = TreeNode(nums[hi])
            t1.left = TreeNode(nums[lo])
            return t1
        if (hi - lo) == 2:
            t1 = TreeNode(nums[lo + 1])
            t1.left = TreeNode(nums[lo])
            t1.right = TreeNode(nums[hi])
            return t1
        mid = lo + (hi - lo) // 2
        t1 = TreeNode(nums[mid])
        t1.left = self.sorted_array_to_bst(nums,lo, mid - 1)
        t1.right = self.sorted_array_to_bst(nums, mid + 1, hi)
        return t1

    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        return self.sorted_array_to_bst(nums,0,len(nums) - 1)


sol = Solution()
print(sol.sortedArrayToBST([0]))