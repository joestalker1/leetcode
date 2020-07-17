MAX = 1000000001


class Solution:
    def longestSubarray(self, nums, limit):
        if not nums:
            return 0
        dp = [[1] * len(nums) for _ in range(len(nums))]
        max_val = [[0] * len(nums) for _ in range(len(nums))]
        min_val = [[MAX] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            max_val[i][i] = nums[i]
            min_val[i][i] = nums[i]
        max_len = 1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i > 0 and j > 0:
                    if abs(nums[j] - max_val[i - 1][j - 1]) <= limit and abs(nums[j] - min_val[i - 1][j - 1]) <= limit:
                        if dp[i - 1][j - 1] + 1 > dp[i][j]:
                            dp[i][j] = dp[i - 1][j - 1] + 1
                            min_val[i][j] = min(min_val[i][j], min_val[i - 1][j - 1], nums[j])
                            max_val[i][j] = max(max_val[i][j], max_val[i - 1][j - 1], nums[j])
                if i > 0:
                    if dp[i - 1][j] >= dp[i][j]:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
                        min_val[i][j] = min(min_val[i][j], min_val[i - 1][j], nums[j])
                        max_val[i][j] = max(max_val[i][j], max_val[i - 1][j], nums[j])

                if j > 0:
                    if abs(nums[j] - max_val[i][j - 1]) <= limit and abs(nums[j] - min_val[i][j - 1]) <= limit:
                        if dp[i][j - 1] + 1 > dp[i][j]:
                            dp[i][j] = dp[i][j - 1] + 1
                            min_val[i][j] = min(min_val[i][j], min_val[i][j - 1], nums[j])
                            max_val[i][j] = max(max_val[i][j], max_val[i][j - 1], nums[j])
                max_len = max(max_len, dp[i][j])

        return max_len


sol = Solution()
#print(sol.longestSubarray([4, 8, 5, 1, 7, 9], 6))  # 3
print(sol.longestSubarray(nums=[1, 2, 4, 7, 2], limit=5))  # 4
print(sol.longestSubarray([8, 2, 4, 7], 4))  # 2
