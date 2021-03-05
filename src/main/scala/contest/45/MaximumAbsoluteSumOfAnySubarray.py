from math import inf

class Solution:
    def maxAbsoluteSum(self, nums):
        cur_sum1 = 0
        cur_sum2 = 0
        max_sum = -inf
        #find max_sum for positve items
        # find min_sum for negative items
        for i in range(len(nums)):
            cur_sum1 = max(nums[i], cur_sum1 + nums[i])
            cur_sum2 = min(nums[i], cur_sum2 + nums[i])
            max_sum = max(max_sum, cur_sum1, abs(cur_sum2))
        return max_sum

sol = Solution()
print(sol.maxAbsoluteSum([-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9]))#44
print(sol.maxAbsoluteSum([2,-5,1,-4,3,-2]))#8
print(sol.maxAbsoluteSum([1,-3,2,3,-4]))#5
