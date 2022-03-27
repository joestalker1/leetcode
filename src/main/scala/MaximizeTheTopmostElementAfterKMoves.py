class Solution:
    def maximumTop(self, nums, k: int) -> int:
        if len(nums) == 1:
            if k % 2 == 0:
                return nums[0]
            return -1
        if k > len(nums):
            return max(nums)
        # k<= len(nums)
        max_val = -inf
        for i in range(k-1):
            max_val = max(max_val, nums[i])
        max_val = max(max_val, nums[k]) if k < len(nums) else max_val
        return max_val
