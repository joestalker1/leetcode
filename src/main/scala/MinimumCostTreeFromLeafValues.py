class Solution(object):
    def mctFromLeafValues(self, arr):
        if not arr:
            return float('inf')
        dp = [[float('inf')] * len(arr) for _ in range(len(arr))]
        for i in range(len(arr)):
            dp[i][i] = 0
        for l in range(1, len(arr)):
            for i in range(len(arr)):
                j = i + l
                if j >= len(arr):
                    break
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], max(arr[i:k + 1]) * max(arr[k + 1: j + 1]) + dp[i][k] + dp[k+1][j])

        return dp[0][-1]


sol = Solution()
print(sol.mctFromLeafValues([6,2,4]))


