class Solution:
    def minDifference(self, nums, queries):
        N = max(nums)
        ans = []
        dp = [[0] * (N + 1)]

        for num in nums:
            t = dp[-1][:]
            t[num] += 1
            dp.append(t)
        for a, b in queries:
            i = 0
            diff = []
            for x, y in zip(dp[b + 1], dp[a]):
                if x != y:
                    diff.append(i)
                i += 1
            ans.append(min([b - a for a, b in zip(diff, diff[1:])] or [-1]))
        return ans


