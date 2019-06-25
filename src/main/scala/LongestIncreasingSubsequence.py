class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        lis = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                #count number is greater nums[i]
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
        return max(lis)


sol = Solution()
print(sol.lengthOfLIS([4,10,4,3,8,9]))#3

print(sol.lengthOfLIS([10,9,2,5,3,4]))#3