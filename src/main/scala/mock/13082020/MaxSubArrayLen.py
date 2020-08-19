class Solution:
    def maxSubArrayLen(self, nums, k):
        if not nums or k < 1:
            return 0
        max_len = 0
        cur_sum = 0
        m = {}
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum == k:
                max_len = max(max_len, i+1)
            if cur_sum - k in m:
                j = m[cur_sum - k]
                max_len = max(max_len, i - j)
            if cur_sum not in m:
                m[cur_sum] = i
        return max_len