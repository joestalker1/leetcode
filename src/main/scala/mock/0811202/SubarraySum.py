class Solution:
    def subarraySum(self, nums, k: int):
        if not nums and k == 0:
            return 0
        l = 0
        r = 0
        res = 0
        subsum = 0
        while r < len(nums):
            subsum += nums[r]
            while abs(subsum) >= abs(k) and l <= r:
                if subsum == k:
                    res += 1
                subsum -= nums[l]
                l += 1
            r += 1
        return res





