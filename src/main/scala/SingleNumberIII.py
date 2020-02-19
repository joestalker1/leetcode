class Solution:
    def singleNumber(self, nums):
        if not nums:
            return []
        bitmask = 0
        for num in nums:
            bitmask ^= num
        #get rightmost bit
        bitmask = bitmask & (-bitmask)
        x = 0
        for num in nums:
            if x & bitmask:
                x = x ^ num
        return [x, x ^ bitmask]



