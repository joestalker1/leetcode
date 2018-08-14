class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def max_of(self, arr, start, end):
        max_index = 0
        max_item = float("-inf")
        for i in range(start, end + 1):
            if arr[i] > max_item:
                max_item = arr[i]
                max_index = i
        return max_index

    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        def traverse(start, end):
            if start > end:
                return None
            if start == end:
                return TreeNode(nums[start])
            max_index = self.max_of(nums, start, end)
            max_item = nums[max_index]
            node = TreeNode(max_item)
            node.left = traverse(start, max_index - 1)
            node.right = traverse(max_index + 1, end)
            return node
        return traverse(0, len(nums) - 1)


sol = Solution()
print(sol.constructMaximumBinaryTree([3,2,1,6,0,5]))