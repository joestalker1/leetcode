class Solution:
    def singleNonDuplicate(self, nums):
        if not nums:
            return
        x = nums[0]
        for i in range(1, len(nums)):
            x = x ^ nums[i]
        return x

sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(sol.singleNonDuplicate([3,3,7,7,10,11,11]))