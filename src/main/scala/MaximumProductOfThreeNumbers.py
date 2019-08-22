class Solution:
    def maximumProduct(self, nums):
        if not nums or len(nums) < 3:
            return None
        nums.sort()
        if nums[0] < 0 and nums[len(nums) - 1] > 0:
            return max(nums[0] * nums[1] * nums[len(nums) - 1], nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3])
        return nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3]


sol = Solution()
print(sol.maximumProduct([-4,-3,-2,-1,60]))