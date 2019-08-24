class Solution:
     def numSubarrayProductLessThanK(self, nums, k):
        if not nums or k <= 1:
            return 0
        prod = 1
        left = 0
        sub_arr_count = 0
        for i in range(len(nums)):
            prod *= nums[i]
            while prod >= k:
                prod /= nums[left]
                left += 1
            sub_arr_count += i - left + 1
        return sub_arr_count


sol = Solution()
print(sol.numSubarrayProductLessThanK([1, 2, 3], 0))
print(sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100))

