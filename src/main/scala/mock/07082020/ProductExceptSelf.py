class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return nums

        output = [0] * len(nums)

