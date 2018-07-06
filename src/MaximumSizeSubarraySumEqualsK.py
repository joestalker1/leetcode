class Solution:
    def maxSubArrayLen(self, nums, k):
        if not nums:
            return 0
        max_cnt = 0
        sum = 0
        j = 0
        for i in range(len(nums)):
            if sum + nums[i] <= k:
                sum += nums[i]
            else:
                sum = sum - nums[j] + nums[i]
                j += 1
            if sum == k:
                max_cnt = max(i - j + 1, max_cnt)
        return max_cnt

sol = Solution()
#print(sol.maxSubArrayLen([0,0], 0))
print(sol.maxSubArrayLen([1, -1, 5, -2, 3], 3))
print(sol.maxSubArrayLen([-2, -1, 2, 1], 1))