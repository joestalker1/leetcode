class Solution:
    def countSpecialSubsequences(self, nums) -> int:
        MOD = 10 ** 9 + 7
        dp0 = 0
        dp1 = 0
        dp2 = 0
        if nums[0] == 0:
            dp0 += 1
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp0 = (2*dp0 + 1) % MOD
            elif nums[i] == 1:
                dp1 = (2 * dp1 + dp0) % MOD
            else:
                dp2 = (2 * dp2 + dp1) % MOD
        return dp2
