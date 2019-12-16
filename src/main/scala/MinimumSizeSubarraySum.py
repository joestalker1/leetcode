class Solution:
    def minSubArrayLen(self, s, nums):
        if not s or not nums:
            return 0
        cur_sum = 0
        min_len = float('inf')
        j = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            while cur_sum >= s:
                min_len = min(min_len, i - j + 1)
                cur_sum -= nums[j]
                j += 1
        return min_len


sol = Solution()
print(sol.minSubArrayLen(11, [1,2,3,4,5]))#3
print(sol.minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]))