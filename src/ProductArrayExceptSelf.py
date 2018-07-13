class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return []
        products = [0 for _ in range(len(nums))]
        products[0] = 1
        for i in range(1, len(nums)):
            products[i] = nums[i - 1]* products[i - 1]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] = right * products[i]
            right = right * nums[i]
        return products

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))




