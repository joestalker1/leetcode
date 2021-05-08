from collections import defaultdict

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sum_arr = sum(nums)
        if sum_arr % p == 0:
            return 0
        min_size = len(nums)
        m = defaultdict(int)
        # removed subarray % p = sum_arr % p
        r = sum_arr % p
        m[0] = -1
        s = 0
        for i in range(len(nums)):
            # module sum
            s += nums[i]
            # find s1 % p = (s - r) % p => r
            k = (s - r) % p
            if k in m:
                min_size = min(min_size, i - m[k])
            m[s % p] = i
        return min_size if min_size!= len(nums) else -1
