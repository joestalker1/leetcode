class Solution:
    def singleNumber(self, nums):
        if not nums:
            return None
        seen1 = 0
        seen2 = 0
        for num in nums:
            seen1 = ~seen2 & (seen1 ^ num)
            seen2 = ~seen1 & (seen2 ^ num)
        return seen1


sol = Solution()
print(sol.singleNumber([2,2,3,2]))
