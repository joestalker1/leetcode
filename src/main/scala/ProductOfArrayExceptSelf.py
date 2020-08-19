class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return nums
        # initial products
        res = [1] * len(nums)
        left_product = 1
        # go from left, multiply bu left_produc - product from 0 till i - 1
        for i in range(len(nums)):
            res[i] *= left_product
            left_product *= nums[i]
        right_product = 1
        # it needs to multiply product on right nums
        # go from right: product[i] = right, right = product of from len-1: i + 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        return res


sol = Solution()
print(sol.productExceptSelf([1,1,1]))
print(sol.productExceptSelf([1,2,3,4]))#[24,12,8,6]


