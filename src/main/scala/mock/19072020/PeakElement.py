MAX = float('inf')
class Solution:
    def findPeakElement(self, nums):
        if not nums:
            return None
        nums.append(-MAX)
        nums.insert(0, -MAX)
        for i in range(len(nums)):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i
        return None
