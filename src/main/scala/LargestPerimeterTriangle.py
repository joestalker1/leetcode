class Solution:
    def largestPerimeter(self, nums) -> int:
        if not nums:
            return 0
        nums.sort()
        max_per = 0
        for i in range(len(nums) - 2):
            if nums[i] + nums[i+1] > nums[i+2]:
                max_per = max(max_per, nums[i] + nums[i+1] + nums[i+2])
        return max_per