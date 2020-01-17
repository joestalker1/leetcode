class Solution:
    def max_sum(self, arr):
        if not arr:
            return None
        dp = [float('inf')] * len(arr)
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            dp[i] = max(arr[i], arr[i] + dp[i - 1])
        return max(dp)


sol = Solution()
print(sol.max_sum([-15, 8, -2, 1, 0, 6, -3]))
