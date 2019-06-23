class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [0] * len(nums)
        for i in range(len(dp)):
            dp[i] = [0] * len(nums)
            dp[i][i] = 1
        last_val = {}
        for i in range(len(nums)):
            last_val[(i, i)] = nums[i]
        max_len = 1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                dp[(i, j)] = 0
                if (i, j - 1) in dp and dp[(i, j - 1)] > dp[(i, j)]:
                    dp[(i, j)] = dp[(i, j - 1)]
                    if (i, j - 1) in last_val and last_val[(i, j - 1)] < nums[j]:
                        dp[(i, j)] = dp[(i, j - 1)] + 1
                        last_val[(i, j)] = nums[j]

                if (i + 1, j - 1) in dp and dp[(i + 1, j - 1)] > dp[(i, j)]:
                    dp[(i, j)] = dp[(i + 1, j - 1)]
                    if (i + 1, j - 1) in last_val and last_val[(i + 1, j - 1)] < nums[j]:
                        dp[(i, j)] = dp[(i + 1, j - 1)] + 1
                        last_val[(i, j)] = nums[j]

                if (i + 1, j) in dp and dp[(i + 1, j)] > dp[(i, j)]:
                    dp[(i, j)] = dp[(i + 1, j)]
                    if (i + 1, j) in last_val and last_val[(i + 1, j)] < nums[j]:
                        dp[(i, j)] = dp[(i + 1, j)] + 1
                        last_val[(i, j)] = nums[j]

                max_len = max(max_len, dp[(i, j)])
        return max_len


sol = Solution()
print(sol.lengthOfLIS([]))
print(sol.lengthOfLIS([1]))
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
