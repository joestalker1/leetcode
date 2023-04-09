class Solution:
    def minImpossibleOR(self, nums) -> int:
        return self._minImpossibleOR(nums)

    def _minImpossibleOR(self, nums) -> int:
        if not nums:
            return 0
        uniq_num = set(nums)
        for i in range(32):
            num = 2 ** i
            if num not in uniq_num:
                return num
        return 0

