class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        sub_len = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                sub_len[i] = sub_len[i-1] + 1
        return max(l for l in sub_len)




