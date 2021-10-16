class Solution:
    def arraySign(self, nums) -> int:
        if not nums:
            return -1

        product = 1
        for a in nums:
            product *= a

        if product < 0:
            return -1
        return 0 if product == 0 else 1
