class Solution:
    def minimizeArrayValue(self, nums) -> int:
        if not nums:
            return 0
        lo = 0
        hi = 10 ** 9

        def is_max(nums, max_val):
            diff = 0
            for i in range(len(nums) - 1, -1, -1):
                num = nums[i]
                num += diff
                diff = 0
                if num >= max_val:
                    diff = num - max_val
            return diff == 0

        while lo < hi:
            cand = lo + (hi - lo) // 2
            if is_max(nums, cand):
                hi = cand
            else:
                lo = cand + 1
        return lo