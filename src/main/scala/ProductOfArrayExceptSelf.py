class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return nums
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i-1]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res


sol = Solution()
print(sol.productExceptSelf([1,1,1]))
print(sol.productExceptSelf([1,2,3,4]))#[24,12,8,6]


