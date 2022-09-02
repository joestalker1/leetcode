class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        if not nums:
            return 0
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for comb_sum in range(target + 1):
            for num in nums:
                if comb_sum - num < 0:
                    break
                dp[comb_sum] += dp[comb_sum - num]
        return dp[target]
