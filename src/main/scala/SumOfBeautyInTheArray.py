class Solution:
    def sumOfBeauties(self, nums) -> int:
        if not nums:
            return 0
        left = [0] * len(nums)
        left[0] = nums[0]
        for i in range(1, len(nums)):
            left[i] = max(nums[i],left[i-1])
        right = [0] * len(nums)
        right[-1] = nums[-1]
        for i in range(len(nums) - 2,-1,-1):
            right[i] = min(nums[i], right[i+1])
        sum_beauty = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > left[i-1] and nums[i] < right[i+1]:
                sum_beauty += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                sum_beauty += 1
        return sum_beauty


sol = Solution()
print(sol.sumOfBeauties([1,2,3,4,5,7,8,9,10]))#14