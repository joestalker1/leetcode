class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        dp = [1] * 5
        for i in range(1,n):
            new_dp = [0] * 5
            new_dp[0] = dp[0] + dp[1] + dp[2] + dp[3]+ dp[4]
            new_dp[1] = new_dp[0] - dp[0]
            new_dp[2] = new_dp[1] - dp[1]
            new_dp[3] = new_dp[2] - dp[2]
            new_dp[4] = 1
            dp = new_dp
        return sum(dp)
