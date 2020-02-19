class Solution:
    def findPeakElement(self, nums):
        if not nums:
            return None
        for i in range(len(nums)):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1

