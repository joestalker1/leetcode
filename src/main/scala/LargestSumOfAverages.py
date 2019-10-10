class Solution:
    def largestSumOfAverages(self, A, K):
        n = len(A)
        dp = [0] * n
        presum = [0]
        for x in A:
            presum.append(presum[-1] + x)
        for i in range(len(dp)):
            dp[i] = float(presum[n] - presum[i]) / (n - i)  # max average for [i, n]

        for k in range(0, K - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    # propogate new data from left to the right
                    dp[i] = max(dp[i], (presum[j] - presum[i]) / (j - i) + dp[j])
        return dp[0]


sol = Solution()
#print(sol.largestSumOfAverages([7959,4983,5994,4877,705,3404,472,3700,2677,5242,3011,2077,9160,4218,3456,176,3425,2669,6622,4808], 19))
#print(sol.largestSumOfAverages([1], 1))
#print(sol.largestSumOfAverages([4,1,7,5,6,2,3], 4))
#print(sol.largestSumOfAverages([1,2,3,4,5,6,7], 4))
print(sol.largestSumOfAverages([9,1,2,3,9], 3))










