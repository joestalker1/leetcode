class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return []
        max_so_far = 0
        max_sum = float('-inf')
        i = 0
        while i < len(nums):
            max_so_far += nums[i]
            max_sum = max(max_sum, max_so_far)
            if max_so_far < 0:
                max_so_far = 0
            i += 1
        return max_sum


sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))