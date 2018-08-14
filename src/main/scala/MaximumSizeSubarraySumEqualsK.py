class Solution:
    def maxSubArrayLen(self, nums, k):
        if not nums:
            return 0
        sum_to_index = {}
        sum = 0
        max_cnt = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                max_cnt = max(i + 1, max_cnt)
            diff = sum - k
            if diff in sum_to_index:
                max_cnt = max(max_cnt, i - sum_to_index[diff])
            if sum not in sum_to_index:
                sum_to_index[sum] = i
        return max_cnt

sol = Solution()
print(sol.maxSubArrayLen([1,0,-1], -1))
print(sol.maxSubArrayLen([1, -1, 5, -2, 3], 3))
print(sol.maxSubArrayLen([-2, -1, 2, 1], 1))
print(sol.maxSubArrayLen([0, 0], 0))