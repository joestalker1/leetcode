class Solution:
    def moveZeroes(self, nums):
        if not nums:
            return nums
        zeros = sum([1 for a in nums if a == 0])
        l = -1
        for r in range(len(nums)):
            if nums[r] == 0 and l == -1:
                l = r
            elif nums[r] != 0 and l != -1:
                nums[l] = nums[r]
                l += 1
        for j in range(zeros):
            nums[-(j+1)] = 0
        return nums


sol = Solution()
print(sol.moveZeroes([4,2,4,0,0,3,0,5,1,0]))





