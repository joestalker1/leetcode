from math import inf

class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        if len(nums) < 2:
            return 0
        min_val = inf
        max_val = -inf
        #find min in wrong position
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                min_val = min(min_val, nums[i])
        #find max in wrong position
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1] < nums[i]:
                max_val = max(max_val, nums[i])
        l = 0
        #find original pos of min_val
        for l in range(len(nums)):
            if nums[l] > min_val:
                break
        r = 0
        #find original pos of max_val
        for r in range(len(nums) - 1, -1, -1):
            if nums[r] < max_val:
                break
        return 0 if r - l <0 else r - l + 1