class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return []
        #local maximum
        max_so_far = 0
        #global maximum
        max_sum = float('-inf')
        for i in range(len(nums)):
            # choice new maximum: current item, max_so_far + current
            max_so_far = max(nums[i], max_so_far + nums[i])
            #calculate global sum
            max_sum = max(max_so_far, max_sum)
        return max_sum


sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))#6