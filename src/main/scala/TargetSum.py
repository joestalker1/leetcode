class Solution:
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dp = [0] * len(nums)
        for i in range(len(dp)):
            dp[i] = [0] * 2001
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, len(nums)):
            for s in range(-1000, 1001):
                if dp[i - 1][1000 + s] > 0:
                    dp[i][s + nums[i] + 1000] += dp[i-1][1000 + s]
                    dp[i][s - nums[i] + 1000] += dp[i-1][1000 + s]
        return dp[len(nums) - 1][S + 1000]



sol = Solution()
#print(sol.findTargetSumWays([45,18,27,39,42,19,1,35,32,16,7,6,25,41,27,18,38,6,42,10], 49))
#print(sol.findTargetSumWays([27,22,39,22,40,32,44,45,46,8,8,21,27,8,11,29,16,15,41,0], 10))
print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))

