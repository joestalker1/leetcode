class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        MOD = 10 ** 9 + 7
        num_to_pos = {}
        dp = [1] * len(arr)
        arr.sort()
        for i, a in enumerate(arr):
            num_to_pos[a] = i

        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    x = arr[i] // arr[j]
                    if x in num_to_pos:
                        dp[i] += dp[j] * dp[num_to_pos[x]]
                        dp[i] = dp[i] % MOD
        return sum(dp) % MOD
    