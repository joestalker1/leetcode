import math

class Solution:
    def maximumXOR(self, nums) -> int:
        # assert self._maximumXOR([1,1]) == 1,'test1'
        # assert self._maximumXOR([1]) == 1,'test2'
        # assert self._maximumXOR([3,2,4,6]) == 7,'test3'
        return self._maximumXOR(nums)

    def _maximumXOR(self, nums) -> int:
        if len(nums) < 2:
            return nums[0] if nums else 0
        res = 0
        max_val = max(nums)
        max_bits = int(math.log2(max_val)) + 1
        for i in range(max_bits):
            for num in nums:
                if (num >> i) & 1:
                    res += (1 << i)
                    break
        return res
